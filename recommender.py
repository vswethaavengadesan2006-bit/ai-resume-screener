import csv
import spacy

nlp = spacy.load("en_core_web_sm")

skill_synonyms = {
    "javascript": ["js", "javascript"],
    "node.js": ["node", "node.js"],
    "express.js": ["express", "express.js"],
    "oop": ["object oriented programming", "oop"],
    "dsa": ["data structures", "dsa"],
    "dbms": ["dbms", "database management"],
    "python": ["python", "py"],
    "c++": ["c++", "cpp"],
    "asp.net": ["asp.net", ".net"],
    "wordpress": ["wordpress"],
    "java": ["java"],
    "sql": ["sql", "database"],
    "html": ["html"],
    "css": ["css"],
    "cn": ["computer networks", "cn"]
}

def recommend_jobs_smart(user_skills):
    recommendations = []

    # Normalize user skills
    normalized_skills = set()
    for skill in user_skills:
        skill_lower = skill.lower()
        for key, synonyms in skill_synonyms.items():
            if skill_lower in synonyms:
                normalized_skills.add(key)

    with open("job_roles.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            job = row["JobRole"]
            required_skills = row["Skills"].split()
            normalized_required = set()
            for skill in required_skills:
                skill_lower = skill.lower()
                for key, synonyms in skill_synonyms.items():
                    if skill_lower in synonyms:
                        normalized_required.add(key)

            matched = normalized_skills.intersection(normalized_required)
            score = round((len(matched) / len(normalized_required)) * 100)
            if score > 0:
                recommendations.append((job, score))

    recommendations.sort(key=lambda x: x[1], reverse=True)
    return recommendations
