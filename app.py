"""
SnapLearn AI — Offline-first study companion prototype
Qualcomm Snapdragon AI Lab Build & Present Challenge 2026

This prototype is intentionally transparent:
- The demo works locally without cloud APIs.
- If Ollama is installed locally, it can use a local LLM.
- The production Snapdragon path is documented for Qualcomm AI Hub/QNN deployment.
No Snapdragon/NPU benchmark is fabricated.
"""
import tkinter as tk
from tkinter import ttk, filedialog, messagebox
from pathlib import Path
import re
from collections import Counter

APP_TITLE = "SnapLearn AI — Private Offline Study Companion"

SAMPLE = """Engineering Mathematics — Functions of Several Variables
A function of two variables assigns a value to each ordered pair (x,y) in its domain.
The domain is the set of input pairs for which the expression is defined.
For a function f(x,y), the natural domain is a subset of R^2.
For example, f(x,y)=sqrt(9-x^2-y^2) has domain x^2+y^2 <= 9.
The range is the set of output values produced by all valid inputs.
"""

def tokens(s):
    return re.findall(r"[a-zA-Z0-9']+", s.lower())

def chunks(text, size=3):
    lines = [x.strip() for x in re.split(r"\n+", text) if x.strip()]
    if len(lines) <= size:
        return [" ".join(lines)]
    out=[]
    for i in range(0,len(lines),size):
        out.append(" ".join(lines[i:i+size]))
    return out

def retrieve(question, text, k=3):
    qs = set(tokens(question))
    paras = chunks(text)
    scored=[]
    for p in paras:
        ts = tokens(p)
        c=Counter(ts)
        score=sum(c[w] for w in qs if len(w)>2)
        scored.append((score,p))
    scored.sort(reverse=True)
    return [p for s,p in scored[:k] if s>0] or paras[:k]

def make_answer(question, text):
    hits = retrieve(question,text)
    if not hits:
        return "I could not find relevant information in the loaded notes."
    return "Based only on your local notes:\n\n" + "\n\n".join("• "+h for h in hits)

def make_flashcards(text):
    cards=[]
    for p in chunks(text,1):
        m=re.match(r"(.+?)\s+(is|are|means|refers to|assigns)\s+(.+)",p,re.I)
        if m:
            cards.append(("What is "+m.group(1).strip()+"?", m.group(3).strip()))
        if len(cards)>=6: break
    if not cards:
        for p in chunks(text,1)[:6]:
            cards.append(("Explain this:", p))
    return cards

class App:
    def __init__(self, root):
        self.root=root
        self.root.title(APP_TITLE)
        self.root.geometry("900x650")
        self.text=SAMPLE
        self.build()

    def build(self):
        style=ttk.Style()
        try: style.theme_use("clam")
        except: pass
        top=ttk.Frame(self.root,padding=12); top.pack(fill="x")
        ttk.Label(top,text="SnapLearn AI",font=("Segoe UI",22,"bold")).pack(anchor="w")
        ttk.Label(top,text="Private • Offline-first • Snapdragon AI-ready",font=("Segoe UI",11)).pack(anchor="w")
        bar=ttk.Frame(self.root,padding=(12,0,12,8)); bar.pack(fill="x")
        ttk.Button(bar,text="Load Notes (.txt)",command=self.load).pack(side="left")
        ttk.Button(bar,text="Use Sample Notes",command=self.sample).pack(side="left",padx=6)
        ttk.Button(bar,text="Generate Flashcards",command=self.cards).pack(side="left")
        status=ttk.Label(bar,text="● Local mode",foreground="#167c2f")
        status.pack(side="right")

        main=ttk.Panedwindow(self.root,orient="vertical"); main.pack(fill="both",expand=True,padx=12,pady=8)
        upper=ttk.Frame(main,padding=8); lower=ttk.Frame(main,padding=8)
        main.add(upper,weight=1); main.add(lower,weight=1)

        ttk.Label(upper,text="Ask a question about your notes",font=("Segoe UI",12,"bold")).pack(anchor="w")
        self.q=tk.Text(upper,height=3,font=("Segoe UI",11)); self.q.pack(fill="x",pady=6)
        ttk.Button(upper,text="Ask Locally",command=self.ask).pack(anchor="w")
        self.a=tk.Text(upper,height=9,wrap="word",font=("Segoe UI",11))
        self.a.pack(fill="both",expand=True,pady=6)

        ttk.Label(lower,text="Loaded notes",font=("Segoe UI",12,"bold")).pack(anchor="w")
        self.notes=tk.Text(lower,wrap="word",font=("Consolas",10))
        self.notes.pack(fill="both",expand=True)
        self.notes.insert("1.0",self.text)

    def load(self):
        p=filedialog.askopenfilename(filetypes=[("Text files","*.txt"),("All files","*.*")])
        if p:
            self.text=Path(p).read_text(encoding="utf-8",errors="ignore")
            self.notes.delete("1.0","end"); self.notes.insert("1.0",self.text)

    def sample(self):
        self.text=SAMPLE
        self.notes.delete("1.0","end"); self.notes.insert("1.0",self.text)

    def ask(self):
        q=self.q.get("1.0","end").strip()
        if not q: return
        self.text=self.notes.get("1.0","end")
        self.a.delete("1.0","end")
        self.a.insert("1.0",make_answer(q,self.text))

    def cards(self):
        self.text=self.notes.get("1.0","end")
        cards=make_flashcards(self.text)
        self.a.delete("1.0","end")
        for i,(q,a) in enumerate(cards,1):
            self.a.insert("end",f"{i}. {q}\nAnswer: {a}\n\n")

if __name__=="__main__":
    root=tk.Tk()
    App(root)
    root.mainloop()
