from flask import Flask, render_template, request
import os
import pandas as pd

from utils import extract_text_from_pdf, preprocess_text
from model import final_match_score

app = Flask(__name__)

UPLOAD_FOLDER = "uploads"
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

SELECTION_THRESHOLD = 60  # %


# Load skills dataset ONCE
skills_df = pd.read_csv("datas/skills/skills_dataset.csv")
JOB_ROLES = sorted(skills_df["job_role"].unique())


@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        resume_files = request.files.getlist("resumes")
        job_description = request.form["job_description"]
        job_role = request.form["job_role"]

        job_clean = preprocess_text(job_description)

        # 🔹 Filter skills by selected job role
        skills = skills_df[
            skills_df["job_role"] == job_role
        ]["skill"].tolist()

        selected = []
        not_selected = []

        for resume in resume_files:
            resume_path = os.path.join(UPLOAD_FOLDER, resume.filename)
            resume.save(resume_path)

            resume_raw = extract_text_from_pdf(resume_path)
            resume_clean = preprocess_text(resume_raw)

            score, matched_skills = final_match_score(
                resume_clean, job_clean, skills
            )

            result = {
                "name": resume.filename,
                "score": score,
                "matched_skills": matched_skills,
                "missing_skills": [s for s in skills if s not in matched_skills]
            }

            if score >= SELECTION_THRESHOLD:
                selected.append(result)
            else:
                not_selected.append(result)

        return render_template(
            "results.html",
            selected=selected,
            not_selected=not_selected,
            threshold=SELECTION_THRESHOLD,
            job_role=job_role.replace("_", " ").title()
        )

    # 🔹 Pass job roles to UI
    return render_template(
        "index.html",
        job_roles=JOB_ROLES
    )


if __name__ == "__main__":
    app.run(debug=True)
