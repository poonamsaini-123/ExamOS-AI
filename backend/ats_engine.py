import re

def calculate_ats_score(text):

    score = 0

    # length check
    if len(text) > 1000:
        score += 20

    # keywords
    keywords = ["python", "sql", "machine learning", "fastapi", "api", "project"]
    found = sum(1 for k in keywords if k.lower() in text.lower())

    score += found * 10

    # formatting signals
    if re.search(r"\bexperience\b", text.lower()):
        score += 10

    if re.search(r"\beducation\b", text.lower()):
        score += 10

    return min(score, 100)