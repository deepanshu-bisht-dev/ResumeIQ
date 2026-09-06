"""
Scores how well a resume matches a given job description using
TF-IDF vectorization + cosine similarity. This is a classic,
lightweight NLP technique - no heavy model download required,
which keeps the app fast to install and run.
"""

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from data.skills_list import SKILLS_LIST
import re


def compute_match_score(resume_text: str, job_description: str) -> float:
    """
    Returns a 0-100 similarity score between the resume and job description.
    """
    if not job_description or not job_description.strip():
        return 0.0

    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([resume_text, job_description])

    similarity = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:2])[0][0]
    return round(float(similarity) * 100, 2)


def find_missing_skills(resume_skills: list, job_description: str) -> list:
    """
    Checks which predefined skills appear in the job description but
    were NOT found in the resume - a simple "skills gap" indicator.
    """
    if not job_description:
        return []

    jd_lower = job_description.lower()
    resume_skills_lower = {s.lower() for s in resume_skills}
    missing = []

    for skill in SKILLS_LIST:
        pattern = r"(?<![a-zA-Z0-9])" + re.escape(skill.lower()) + r"(?![a-zA-Z0-9])"
        mentioned_in_jd = re.search(pattern, jd_lower) is not None

        if mentioned_in_jd and skill.lower() not in resume_skills_lower:
            missing.append(skill)

    return missing
