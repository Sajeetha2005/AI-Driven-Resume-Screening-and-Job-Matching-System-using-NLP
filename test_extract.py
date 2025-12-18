from utils import extract_text_from_pdf, preprocess_text

# Path to resume
resume_path = "datas/resume/Sajee Resume.pdf"

# Extract raw text
raw_text = extract_text_from_pdf(resume_path)

print("========== RAW TEXT ==========")
print(raw_text[:500])

# Preprocess text
clean_text = preprocess_text(raw_text)

print("\n========== CLEAN TEXT ==========")
print(clean_text[:500])
