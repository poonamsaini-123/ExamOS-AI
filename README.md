# ExamOS-AI

An AI-powered exam preparation assistant that helps users analyze resumes, process PDFs, and interact with AI for academic support.

## Features

* 📄 PDF reading and text extraction
* 🤖 AI-powered responses using Gemini
* 📊 ATS resume analysis
* 🌐 Simple web interface
* 📁 Clean backend and frontend structure

## Project Structure

```
ExamOS-AI/
│
├── agents/
│   └── examos-agent/
│       ├── examos-agent.json
│       └── instruction.md
│
├── backend/
│   ├── __init__.py
│   ├── ats_engine.py
│   ├── gemini_service.py
│   ├── main.py
│   └── pdf_reader.py
│
├── frontend/
│   ├── index.html
│   ├── script.js
│   └── style.css
│
├── .gitignore
├── LICENSE
├── README.md
└── requirements.txt
```

## Installation

1. Clone the repository

```bash
git clone https://github.com/poonamsaini-123/ExamOS-AI.git
```

2. Install dependencies

```bash
pip install -r requirements.txt
```

3. Create a `.env` file and add your API keys.

4. Run the application

```bash
python backend/main.py
```

## Technologies Used

* Python
* HTML
* CSS
* JavaScript
* Google Gemini API

## Author

**Poonam Saini**

GitHub: https://github.com/poonamsaini-123
