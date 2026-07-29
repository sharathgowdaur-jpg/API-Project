import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()

client = Groq(api_key=os.getenv("GROQ_API_KEY"))

def generate_function(job_role, experience_level, skills, num_questions=10):

    prompt = f"""
You are an expert interviewer.

Generate {num_questions} interview questions for a
{experience_level} {job_role}
with the following skills: {skills}.

Distribution:
- 50% Technical
- 30% Behavioral (start with "Tell me about a time when...")
- 20% Situational (start with "What would you do if...")

For each question use exactly this format:

Q[number]: [Question]

TYPE: Technical / Behavioral / Situational

DIFFICULTY: Easy / Medium / Hard

GOOD_ANSWER: keyword1, keyword2, keyword3
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"You are an expert interviewer specializing in {job_role} roles."
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7,
        max_completion_tokens=2048,
    )

    return response.choices[0].message.content