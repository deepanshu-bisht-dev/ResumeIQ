"""
Extracts structured information from resume text:
- Name (via spaCy Named Entity Recognition)
- Email, phone, LinkedIn/GitHub links (via regex)
- Skills (via keyword matching against a predefined list)
- Education (via section detection + degree keyword matching)
"""

import re
import spacy
from data.skills_list import SKILLS_LIST

# Loaded once at import time - the small English model is enough for
# name/entity extraction and keeps the app lightweight to install.
_nlp = spacy.load("en_core_web_sm")

_EMAIL_RE = re.compile(r"[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}")
_PHONE_RE = re.compile(r"(\+?\d{1,3}[-.\s]?)?\(?\d{3,5}\)?[-.\s]?\d{3,4}[-.\s]?\d{3,4}")
_LINKEDIN_RE = re.compile(r"(https?://)?(www\.)?linkedin\.com/in/[A-Za-z0-9\-_/]+", re.IGNORECASE)
_GITHUB_RE = re.compile(r"(https?://)?(www\.)?github\.com/[A-Za-z0-9\-_/]+", re.IGNORECASE)

_DEGREE_KEYWORDS = [
    "B.Tech", "M.Tech", "Bachelor", "Master", "B.Sc", "M.Sc", "B.E.",
    "M.E.", "PhD", "MBA", "BCA", "MCA", "Diploma", "B.A.", "M.A.",
]


def extract_name(text: str) -> str:
    """
    Uses spaCy NER to find the most likely candidate name -
    typically the first PERSON entity near the top of the resume.
    """
    # Only scan the first ~300 characters - names appear at the top,
    # and scanning the full doc risks picking up a referenced person's name.
    header_text = text[:300]
    doc = _nlp(header_text)

    for ent in doc.ents:
        if ent.label_ == "PERSON":
            return ent.text.strip()

    return "Not found"


def extract_email(text: str) -> str:
    match = _EMAIL_RE.search(text)
    return match.group(0) if match else "Not found"


def extract_phone(text: str) -> str:
    match = _PHONE_RE.search(text)
    return match.group(0).strip() if match else "Not found"


def extract_links(text: str) -> dict:
    linkedin = _LINKEDIN_RE.search(text)
    github = _GITHUB_RE.search(text)
    return {
        "linkedin": linkedin.group(0) if linkedin else None,
        "github": github.group(0) if github else None,
    }


def extract_skills(text: str) -> list:
    """
    Matches predefined skills against the resume text (case-insensitive,
    whole-phrase matching to avoid partial-word false positives like
    'C' matching inside 'Communication').
    """
    found = []
    text_lower = text.lower()

    for skill in SKILLS_LIST:
        pattern = r"(?<![a-zA-Z0-9])" + re.escape(skill.lower()) + r"(?![a-zA-Z0-9])"
        if re.search(pattern, text_lower):
            found.append(skill)

    return found


def extract_education(text: str) -> list:
    """
    Finds lines mentioning common degree keywords, returning up to
    3 relevant lines as a lightweight education summary.
    """
    lines = text.split("\n")
    education_lines = []

    for line in lines:
        if any(keyword.lower() in line.lower() for keyword in _DEGREE_KEYWORDS):
            cleaned = line.strip()
            if cleaned and cleaned not in education_lines:
                education_lines.append(cleaned)

    return education_lines[:3]


def extract_all(text: str) -> dict:
    """
    Runs all extractors and returns a single structured result.
    """
    return {
        "name": extract_name(text),
        "email": extract_email(text),
        "phone": extract_phone(text),
        "links": extract_links(text),
        "skills": extract_skills(text),
        "education": extract_education(text),
    }
