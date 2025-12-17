# app.py
import streamlit as st
from skill_extractor import extract_skills
from recommender import recommend_jobs_nlp
import PyPDF2
import os



# --- Streamlit Page Configuration ---
st.set_page_config(page_title="AI Resume Screener", page_icon=":briefcase:")
st.title("📝 AI Resume Screener & Job Recommender")
st.write("Upload your resume (PDF) and get recommended job roles based on your skills.")

# --- PDF Upload and Processing ---
uploaded_file = st.file_uploader("Choose your resume PDF", type="pdf")

if uploaded_file is not None:
    # Extract text from PDF
    pdf_reader = PyPDF2.PdfReader(uploaded_file)
    resume_text = ""
    for page in pdf_reader.pages:
        resume_text += page.extract_text()
    
    st.subheader("📄 Extracted Resume Text")
    st.write(resume_text)
    
    # Extract skills
    skills_found = extract_skills(resume_text)
    st.subheader("💡 Extracted Skills")
    st.write(skills_found)
    
    # Recommend jobs
    job_recommendations = recommend_jobs_nlp(skills_found)
    st.subheader("🏆 Job Recommendations")
    for job, score in job_recommendations:
        st.write(f"{job} → Match Score: {score}%")
