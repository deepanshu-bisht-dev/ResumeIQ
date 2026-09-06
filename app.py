"""
AI-Powered Resume Analyzer - Flask app.
Upload a resume (PDF/DOCX), extract structured info, and optionally
score it against a pasted job description.
"""

import os
import uuid
from flask import Flask, render_template, request, jsonify

from parser.text_extractor import extract_text
from parser.info_extractor import extract_all
from parser.match_scorer import compute_match_score, find_missing_skills

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, "uploads")
ALLOWED_EXTENSIONS = {"pdf", "docx"}
MAX_CONTENT_LENGTH = 8 * 1024 * 1024  # 8 MB

app = Flask(__name__)
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER
app.config["MAX_CONTENT_LENGTH"] = MAX_CONTENT_LENGTH


def allowed_file(filename: str) -> bool:
    return "." in filename and filename.rsplit(".", 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/api/analyze", methods=["POST"])
def analyze():
    if "resume" not in request.files:
        return jsonify({"error": "No resume file uploaded"}), 400

    file = request.files["resume"]
    job_description = request.form.get("job_description", "").strip()

    if file.filename == "":
        return jsonify({"error": "No file selected"}), 400

    if not allowed_file(file.filename):
        return jsonify({"error": "Unsupported file type. Use PDF or DOCX."}), 400

    ext = file.filename.rsplit(".", 1)[1].lower()
    unique_name = f"{uuid.uuid4().hex}.{ext}"
    filepath = os.path.join(app.config["UPLOAD_FOLDER"], unique_name)
    file.save(filepath)

    try:
        raw_text = extract_text(filepath, ext)

        if not raw_text.strip():
            return jsonify({"error": "Could not extract any text from this file. It may be a scanned image."}), 422

        extracted = extract_all(raw_text)

        result = {
            "name": extracted["name"],
            "email": extracted["email"],
            "phone": extracted["phone"],
            "links": extracted["links"],
            "skills": extracted["skills"],
            "education": extracted["education"],
        }

        if job_description:
            result["match_score"] = compute_match_score(raw_text, job_description)
            result["missing_skills"] = find_missing_skills(extracted["skills"], job_description)
        else:
            result["match_score"] = None
            result["missing_skills"] = []

    except Exception as e:
        return jsonify({"error": f"Could not process resume: {str(e)}"}), 500
    finally:
        # Clean up the uploaded file after processing - we don't need to keep it
        if os.path.exists(filepath):
            os.remove(filepath)

    return jsonify(result)


@app.route("/health")
def health():
    return jsonify({"status": "ok"})


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5002, debug=True)
