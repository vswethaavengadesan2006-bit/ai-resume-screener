import re

def extract_skills(resume_text):
    resume_text = resume_text.lower()

    skills = {
        "c", "c++", "java", "python", "html", "css", "javascript",
        "sql", "mysql", "node.js", "express.js", "wordpress",
        "oop", "dsa", "dbms", "cn", "asp.net"
    }

    extracted = []
    for skill in skills:
        pattern = r"\b" + re.escape(skill) + r"\b"
        if re.search(pattern, resume_text):
            extracted.append(skill)

    return extracted
