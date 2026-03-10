import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def analyze_resume(extracted_text, job_description=""):
    
    prompt = f"""
You are an expert HR consultant and ATS specialist for the Indian job market.

Analyze this resume and provide:

1. ATS SCORE (0-100): How well will this pass ATS filters?
2. KEY SKILLS FOUND: List the technical skills you found
3. MISSING SKILLS: What important skills are missing?
4. JOB MATCH SCORE (0-100): How well does it match the job description?
5. TOP 5 INTERVIEW QUESTIONS: Based on this resume, what will interviewers ask?
6. IMPROVEMENT TIPS: 3 specific suggestions to improve this resume

Resume Text:
{extracted_text}

Job Description:
{job_description if job_description else "Not provided - give general analysis"}

Format your response clearly with each section labeled.
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[
            {
                "role": "user",
                "content": prompt
            }
        ],
        max_tokens=1500
    )
    
    return response.choices[0].message.content
