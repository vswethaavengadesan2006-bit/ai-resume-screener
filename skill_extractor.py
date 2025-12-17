
import spacy
import re
import os

try:
    nlp = spacy.load("en_core_web_sm")
except:
    os.system("python -m spacy download en_core_web_sm")
    nlp = spacy.load("en_core_web_sm")

def extract_skills(resume_text):
    resume_text = resume_text.lower()
    doc = nlp(resume_text)

    skill_patterns = {
        "c": [r"\bc\b"],
        "c++": [r"c\+\+"],
        "java": [r"\bjava\b"],
        "python": [r"\bpython\b"],
        "html": [r"\bhtml\b"],
        "css": [r"\bcss\b"],
        "javascript": [r"\bjavascript\b", r"\bjs\b"],
        "sql": [r"\bsql\b"],
        "mysql": [r"\bmysql\b"],
        "node.js": [r"\bnode\.?js\b"],
        "express.js": [r"\bexpress\.?js\b"],
        "wordpress": [r"\bwordpress\b"],
        "oop": [r"object[-\s]oriented programming", r"\boop\b"],
        "dsa": [r"data structures", r"\bdsa\b"],
        "dbms": [r"\bdbms\b", r"database management"],
        "cn": [r"computer networks"],
        "asp.net": [r"asp\.net", r"\.net"]
    }

    extracted_skills = set()

    for skill, patterns in skill_patterns.items():
        for pattern in patterns:
            if re.search(pattern, resume_text):
                extracted_skills.add(skill)

    return list(extracted_skills)
