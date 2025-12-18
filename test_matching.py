from utils import extract_text_from_pdf, preprocess_text
from model import final_match_score

# Load resume
resume_raw = extract_text_from_pdf("datas/resume/Sajee Resume.pdf")
resume_clean = preprocess_text(resume_raw)

# Load job description
with open("datas/job_descriptions/ml_engineer.txt", "r") as file:
    job_text = file.read()
job_clean = preprocess_text(job_text)

# Load skills
with open("datas/skills/skills.txt") as file:
    skills = [line.strip() for line in file if line.strip()]

score, matched_skills = final_match_score(resume_clean, job_clean, skills)

print(f"Final Match Score: {score}%")
print("Matched Skills:", matched_skills)
