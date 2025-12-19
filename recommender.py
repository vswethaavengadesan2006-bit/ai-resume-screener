import csv

def recommend_jobs_nlp(user_skills):
    recommendations = []

    # Convert user skills to lowercase set
    user_skills = set(skill.lower() for skill in user_skills)

    with open("job_roles.csv", "r") as file:
        reader = csv.DictReader(file)

        for row in reader:
            job_role = row["JobRole"]
            required_skills = set(
                skill.strip().lower() for skill in row["Skills"].split(",")
            )

            # Find matched skills
            matched_skills = user_skills.intersection(required_skills)

            # Calculate match percentage
            if len(required_skills) > 0:
                match_percentage = round(
                    (len(matched_skills) / len(required_skills)) * 100
                )
            else:
                match_percentage = 0

            if match_percentage > 0:
                recommendations.append(
                    (job_role, match_percentage, list(matched_skills))
                )

    # Sort by match percentage (highest first)
    recommendations.sort(key=lambda x: x[1], reverse=True)

    return recommendations
