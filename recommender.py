import csv
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def recommend_jobs_nlp(user_skills):
    jobs = []
    job_skills = []

    with open("job_roles.csv", "r") as file:
        reader = csv.DictReader(file)
        for row in reader:
            jobs.append(row["JobRole"])
            job_skills.append(row["Skills"])

    documents = job_skills + [" ".join(user_skills)]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(documents)

    scores = cosine_similarity(tfidf_matrix[-1], tfidf_matrix[:-1])[0]

    results = []
    for job, score in zip(jobs, scores):
        results.append((job, round(score * 100)))

    results.sort(key=lambda x: x[1], reverse=True)
    return results
