import pandas as pd

base_roles = {
    "machine_learning_engineer": [
        "python", "machine learning", "data analysis", "sql",
        "flask", "model building", "deployment", "statistics",
        "numpy", "pandas"
    ],
    "web_developer": [
        "html", "css", "javascript", "react", "node",
        "api", "sql", "flask", "git"
    ],
    "data_analyst": [
        "python", "sql", "excel", "data analysis",
        "power bi", "tableau", "statistics"
    ]
}

levels = ["junior", "mid", "senior"]
domains = ["healthcare", "fintech", "ecommerce", "education", "research"]

rows = []

for role, skills in base_roles.items():
    for level in levels:
        for domain in domains:
            job_role = f"{level}_{role}_{domain}"
            for skill in skills:
                rows.append({
                    "job_role": job_role,
                    "skill": skill
                })

df = pd.DataFrame(rows)
df.to_csv("datas/skills/skills_dataset.csv", index=False)

print("✅ Large skills dataset created")
print("Total rows:", len(df))
print("Unique job roles:", df['job_role'].nunique())
