# SnapLearn AI — Submission Summary

**Project:** SnapLearn AI — Private Offline Study Companion  
**Target platform:** Snapdragon-powered HP PCs  
**Category:** On-device AI / Education

### Executive summary
SnapLearn AI is a privacy-first study assistant that runs locally on a student's PC. Students can load their own notes, ask natural-language questions, retrieve relevant passages, and generate revision flashcards without sending their notes to a cloud service.

### Problem
Cloud AI study tools depend on connectivity and can require students to upload personal notes. This is inconvenient during poor connectivity and raises privacy concerns for personal or institutional study material.

### Proposed solution
SnapLearn AI uses a local retrieval-and-generation pipeline. The reference prototype demonstrates local note loading, relevance retrieval, grounded answers and flashcards. The production Snapdragon implementation is designed to replace the reference components with Qualcomm AI Hub models and execute supported inference through the Snapdragon Hexagon NPU.

### AI / Snapdragon architecture
Student notes → local parsing/chunking → quantized embedding model (Qualcomm AI Hub) → local vector index → question embedding → relevant passages → on-device small language model (Qualcomm AI Hub) → grounded answer.

Optional: local speech-to-text model for voice questions.

### Privacy
The reference application does not require a cloud API or API key. In the intended production configuration, study material and inference remain on-device.

### Deployment
Designed for Snapdragon-powered HP PCs. The final hardware validation should measure latency, memory, energy use and quality on an actual supported Snapdragon PC. No unsupported benchmark is claimed in this prototype.

### Innovation
The focus is not a generic chatbot; it is a private study workflow around the student's own material: ask, retrieve, revise, quiz and later add voice interaction.

### Current prototype
The included `app.py` is a runnable local reference implementation using only Python's standard library. It proves the core interaction and provides a clear replacement point for AI Hub/QNN inference.

### Roadmap
1. Qualcomm AI Hub embedding model.
2. Quantized on-device LLM.
3. QNN/Hexagon NPU execution.
4. Voice questions.
5. PDF/OCR ingestion.
6. Quiz generation and weak-topic tracking.
7. Real Snapdragon performance benchmark.

### Limitations
The current prototype is a reference demo and does not claim Snapdragon NPU execution. The production AI Hub models and hardware benchmark must be validated on supported Snapdragon HP hardware.

### Compliance note
Only submit if the participant satisfies the official eligibility requirements and owns/has access to the required Snapdragon-powered laptop as stated by the challenge organizer. Do not make a false hardware declaration.
