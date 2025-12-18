from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from utils import preprocess_text   # 👈 IMPORTANT


def tfidf_similarity(resume_text, job_text):
    documents = [resume_text, job_text]
    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    return cosine_similarity(
        tfidf_matrix[0:1], tfidf_matrix[1:2]
    )[0][0]


def skill_overlap_score(resume_text, job_text, skills):
    resume_tokens = set(resume_text.split())
    job_tokens = set(job_text.split())

    matched_skills = []

    for skill in skills:
        # 🔥 PREPROCESS SKILL SAME AS RESUME & JD
        processed_skill = preprocess_text(skill)
        skill_tokens = processed_skill.split()

        resume_match = sum(1 for token in skill_tokens if token in resume_tokens)
        job_match = sum(1 for token in skill_tokens if token in job_tokens)

        if resume_match >= max(1, len(skill_tokens) // 2) and \
           job_match >= max(1, len(skill_tokens) // 2):
            matched_skills.append(skill)

    score = len(matched_skills) / len(skills) if skills else 0
    return score, matched_skills


def final_match_score(resume_text, job_text, skills):
    tfidf_score = tfidf_similarity(resume_text, job_text)
    skill_score, matched_skills = skill_overlap_score(
        resume_text, job_text, skills
    )

    final_score = (0.6 * tfidf_score) + (0.4 * skill_score)
    return round(final_score * 100, 2), matched_skills
