# SnapLearn AI

**Snapdragon® AI Lab Build & Present Challenge 2026 — Solution Submission Prototype**

## One-line idea
SnapLearn AI is a privacy-first, offline study companion that lets students load their own notes and ask questions or generate revision flashcards locally.

## Problem
Students often use cloud AI for studying. This can require an internet connection and may send personal notes to remote services. Students in hostels, classrooms, travel, or low-connectivity areas need a useful local alternative.

## Solution
SnapLearn AI keeps the learning material on the user's PC. The prototype:
- loads local study notes;
- retrieves the most relevant passages for a question;
- gives a grounded answer from those passages;
- generates simple revision flashcards;
- works without a cloud API.

## Snapdragon optimization plan
The production version is designed for Snapdragon-powered HP PCs:
1. Replace the prototype retrieval layer with a quantized embedding model from Qualcomm AI Hub.
2. Use an on-device small language model from Qualcomm AI Hub for grounded answer generation.
3. Use ONNX Runtime with Qualcomm QNN/Hexagon NPU execution where supported.
4. Add local speech input using a compatible AI Hub speech model.
5. Measure CPU vs NPU latency, memory, battery impact and answer quality on an actual Snapdragon HP PC.

**Important:** This submission does not claim that the attached prototype has been benchmarked on a Snapdragon NPU. The current demo is a transparent local reference implementation.

## Run
Windows/macOS/Linux with Python 3:
```bash
python app.py
```
No external package is required for the basic demo.

## Demo
1. Run `python app.py`.
2. Click **Use Sample Notes**.
3. Ask: `Why is the domain a subset of R^2?`
4. Click **Ask Locally**.
5. Click **Generate Flashcards**.

## Suggested 60–90 second demo script
"SnapLearn AI is an offline-first study companion. I load my own notes, ask a question, and the application retrieves only relevant local passages. The answer is grounded in those notes rather than a remote web service. I can also generate revision flashcards. The production architecture is intended for Snapdragon-powered HP PCs: Qualcomm AI Hub models can replace the reference retrieval and generation components and execute through the Snapdragon NPU. The prototype deliberately does not fabricate an NPU benchmark; that benchmark is the next validation step on Snapdragon hardware."

## Evaluation mapping
### Technical Implementation
Local document ingestion, retrieval, grounded response, flashcard generation, modular architecture.

### Application Use Case & Innovation
A student-focused private AI assistant designed around offline access and personal study material.

### Deployment & Accessibility
No cloud account or API key is required for the reference demo. It can run on a normal Windows laptop and is designed to move to Snapdragon NPU execution.

### Presentation & Documentation
Includes this README, architecture diagram, proposal summary and pitch deck.

## Ownership / disclosure
The participant should submit only work they are entitled to submit and should review the challenge's ownership and eligibility rules before submission.
