**Problem Statement: AI-powered Resume Intelligence & Career Guidance**

ExamOS AI is an intelligent resume analysis platform that transforms traditional resumes into actionable career insights using AI.

# 🚀 ExamOS AI – Intelligent Resume Analyzer

> AI-powered Resume Analysis Platform built using **FastAPI**, **Lemma AI**, and **Python** to provide detailed resume insights, ATS evaluation, skill extraction, interview preparation, and personalized career guidance.

![Python](https://img.shields.io/badge/Python-3.11-blue?logo=python)
![FastAPI](https://img.shields.io/badge/FastAPI-Backend-009688?logo=fastapi)
![AI](https://img.shields.io/badge/Lemma-AI-purple)
![License](https://img.shields.io/badge/License-MIT-green)

---

# 📖 Overview

Recruiters spend only a few seconds reviewing each resume.

**ExamOS AI** helps students and job seekers instantly understand how strong their resume is by generating an AI-powered analysis.

The system extracts resume content from a PDF, analyzes it using an AI agent, and produces an easy-to-understand report including:

- Professional Summary
- Skills Extraction
- ATS Evaluation
- Missing Skills
- Resume Improvement Suggestions
- Interview Questions
- Personalized Learning Roadmap

---

# ✨ Features

✅ Upload Resume (PDF)

✅ Automatic Text Extraction

✅ AI-Powered Resume Analysis

✅ ATS Score Calculation

✅ Technical & Soft Skill Extraction

✅ Missing Skill Detection

✅ Resume Improvement Suggestions

✅ Personalized Learning Roadmap

## Architecture Diagram

![Architecture](images/architecture.png)

### Workflow

1. User uploads a resume through the frontend.
2. FastAPI backend receives the PDF.
3. PDF Reader extracts text from the uploaded resume.
4. ATS Engine calculates the ATS score and extracts skills.
5. Gemini AI Service generates detailed AI-powered resume analysis.
6. FastAPI combines all results into a JSON response.
7. The frontend displays the ATS score, skills, missing skills, suggestions, and AI analysis.

✅ Interview Question Generation
