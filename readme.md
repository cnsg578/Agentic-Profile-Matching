# 🤖 AI Resume Matching Agent

🚀 An intelligent **LangGraph-based AI agent** that automates candidate screening, ranking, and hiring recommendations using job descriptions and resume data.

---


## 📌 Project Overview

This project simulates a real-world **AI-powered recruitment assistant** that:

- Understands job descriptions
- Extracts hiring requirements
- Searches candidate resumes using RAG
- Ranks candidates intelligently
- Performs multi-round screening
- Provides explainable hiring decisions
- Supports interactive human feedback

---

## 🧠 Key Features

### 🔍 1. Requirement Extraction
- Parses job descriptions
- Separates **must-have** and **nice-to-have** skills

---

### 📂 2. Resume Search (RAG-Based)
- Retrieves relevant candidates based on requirements
- Easily extendable with **FAISS / Vector DB**

---

### 📊 3. Candidate Ranking
- Scores candidates based on skill match
- Generates reasoning behind ranking

---

### 🥇 4. Multi-Round Screening
- **Round 1:** Top 10 shortlisted
- **Round 2:** Deep evaluation (enhanced scoring)
- **Final Round:** Hire / No-Hire decision

---

### 📈 5. Explainability Engine
- Highlights:
  - Strengths
  - Skill gaps
  - Improvement suggestions
- Provides transparency in decision-making

---

### 🔄 6. Human Feedback Loop
- Allows dynamic updates:
  - Add new skills (e.g., Node.js, AWS)
- Re-ranks candidates based on updated requirements

---

### 💬 7. Conversational Interface (CLI)
Supports natural language queries like:

```bash
Find React developers with 3+ years
Compare top candidates
Why did John rank higher?
Update requirement add Node.js
Generate interview questions