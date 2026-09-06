<div align="center">

# ResumeIQ

**An AI-powered resume analyzer that parses, scores, and matches resumes against job descriptions.**

[![Python](https://img.shields.io/badge/Python-3.12-3776AB?style=for-the-badge&logo=python&logoColor=white)](https://www.python.org/)
[![Flask](https://img.shields.io/badge/Flask-3.0.3-000000?style=for-the-badge&logo=flask&logoColor=white)](https://flask.palletsprojects.com/)
[![spaCy](https://img.shields.io/badge/spaCy-3.7.5-09A3D5?style=for-the-badge&logo=spacy&logoColor=white)](https://spacy.io/)
[![scikit-learn](https://img.shields.io/badge/scikit--learn-1.5.1-F7931E?style=for-the-badge&logo=scikitlearn&logoColor=white)](https://scikit-learn.org/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)](LICENSE)

[![Repo Size](https://img.shields.io/github/repo-size/deepanshu-bisht-dev/ResumeIQ?style=flat-square)](https://github.com/deepanshu-bisht-dev/ResumeIQ)
[![Last Commit](https://img.shields.io/github/last-commit/deepanshu-bisht-dev/ResumeIQ?style=flat-square)](https://github.com/deepanshu-bisht-dev/ResumeIQ/commits/main)
[![Issues](https://img.shields.io/github/issues/deepanshu-bisht-dev/ResumeIQ?style=flat-square)](https://github.com/deepanshu-bisht-dev/ResumeIQ/issues)
[![Stars](https://img.shields.io/github/stars/deepanshu-bisht-dev/ResumeIQ?style=flat-square)](https://github.com/deepanshu-bisht-dev/ResumeIQ/stargazers)

[Features](#-features) • [Getting Started](#-getting-started) • [Usage](#-usage) • [Project Structure](#-project-structure) • [Roadmap](#-roadmap) • [Contributing](#-contributing)

</div>

---

## 📖 About

**ResumeIQ** is a Flask-based web app that reads resumes (PDF/DOCX), extracts structured information using NLP, and scores how well a resume matches a given job description. It's built as a practical tool for job seekers to test and refine their resumes before submitting them — and as a learning project exploring text extraction, entity recognition, and text-similarity scoring.

## ✨ Features

- 📄 **Multi-format parsing** — accepts both `.pdf` and `.docx` resumes
- 🧠 **NLP-based extraction** — pulls names, skills, education, and experience using spaCy
- 🎯 **Job-match scoring** — compares resume content against a job description using scikit-learn text similarity
- 🌐 **Simple web interface** — upload and analyze resumes directly from the browser, no CLI needed
- ⚡ **Fast, local processing** — no external API calls required for parsing

## 🛠️ Tech Stack

| Layer | Technology |
|---|---|
| Backend | ![Flask](https://img.shields.io/badge/Flask-000000?style=flat-square&logo=flask&logoColor=white) |
| PDF Parsing | ![pdfplumber](https://img.shields.io/badge/pdfplumber-0.11.4-informational?style=flat-square) |
| DOCX Parsing | ![python-docx](https://img.shields.io/badge/python--docx-1.1.2-informational?style=flat-square) |
| NLP | ![spaCy](https://img.shields.io/badge/spaCy-09A3D5?style=flat-square&logo=spacy&logoColor=white) |
| Similarity Scoring | ![scikit-learn](https://img.shields.io/badge/scikit--learn-F7931E?style=flat-square&logo=scikitlearn&logoColor=white) |
| Frontend | ![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white) ![CSS3](https://img.shields.io/badge/CSS3-1572B6?style=flat-square&logo=css3&logoColor=white) |

## 🚀 Getting Started

### Prerequisites

- Python **3.12** (recommended — spaCy's dependencies may not have prebuilt wheels for newer versions)
- `pip` and `venv`

### Installation

```bash
# 1. Clone the repository
git clone https://github.com/deepanshu-bisht-dev/ResumeIQ.git
cd ResumeIQ

# 2. Create and activate a virtual environment
py -3.12 -m venv venv
venv\Scripts\Activate.ps1        # Windows (PowerShell)
# source venv/bin/activate       # macOS/Linux

# 3. Install dependencies
python -m pip install --upgrade pip
python -m pip install -r requirements.txt

# 4. Download the spaCy language model
python -m spacy download en_core_web_sm

# 5. Run the app
python -u app.py
```

The app will start on `http://127.0.0.1:5000` by default.

## 📋 Usage

1. Launch the app and open it in your browser
2. Upload a resume (`.pdf` or `.docx`)
3. Paste in the target job description
4. Click **Analyze** to view extracted resume data and a job-match score
5. Use the feedback to refine your resume for that specific role

## 📂 Project Structure

```
ResumeIQ/
├── app.py                    # Flask app entry point
├── requirements.txt          # Python dependencies
├── parser/
│   ├── text_extractor.py     # PDF/DOCX text extraction (pdfplumber, python-docx)
│   └── info_extractor.py     # NLP-based info extraction (spaCy)
├── data/                     # Reference/skill datasets used for matching
├── static/                   # CSS/JS assets
├── templates/                # HTML templates (Jinja2)
├── uploads/                  # Uploaded resume files
└── .gitignore
```

## 🗺️ Roadmap

- [ ] Support for multiple job description comparisons at once
- [ ] Downloadable analysis report (PDF)
- [ ] Skill-gap suggestions based on missing keywords
- [ ] Resume formatting/quality checks (not just keyword match)
- [ ] Deploy a live demo

## 🤝 Contributing

Contributions, issues, and feature requests are welcome!

1. Fork the repo
2. Create your feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📄 License

Distributed under the MIT License. See `LICENSE` for more information.

> Your repo doesn't have a `LICENSE` file yet — add one (GitHub: **Add file → Create new file → LICENSE**, then pick "MIT License" from the template picker) or remove the license badge/section above if you'd rather keep it unlicensed for now.

## 👤 Author

**Deepanshu Bisht**

[![GitHub](https://img.shields.io/badge/GitHub-181717?style=flat-square&logo=github&logoColor=white)](https://github.com/deepanshu-bisht-dev)

---

<div align="center">
<sub>Built while learning AI/ML — feedback and contributions welcome ⭐</sub>
</div>
