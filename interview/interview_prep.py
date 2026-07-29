import os
from dotenv import load_dotenv
from groq import Groq

load_dotenv()
client = Groq(api_key=os.getenv("API_KEY"))

def generate_function(job_role,experince_level,skills,num_questions=10):
    prompt = f"""
    You are an expert interviewer. Generate {num_questions} interview questions for a {experince_level} {job_role} with the following skills: {skills}. 
    The questions should be challenging and relevant to the job role and skills provided. 
    Please provide the questions in a numbered list format.

    distribution of questions should be as follows:
    - 50% technical questions related to their skills
    - 30% behavioral questions (start with "Tell me about a time when...")
    - 20% situational questions (start with "what would you do if ...")

    for each each question follow the exact format:
    Q[number]: [question]
        TYPE:[technical / behavioral / situational]
        difficulty: [easy / medium / hard]
        good_answer: [3-4 keywords or concepts,comma separated]
        Make question specific to the skills.Do not ask generic quesions make difficulty increase gradually from easy to high 
    """

    response = client.chat.completions.create(
        model = "llam-3.3-70b-versatile",
        messages = [
            {
                "role" : "system",
                "content" : "you are an expert interviewer specializing {job_role} roles.Generate questions that accurately reflect what top companies ask"
            },
            {
                "role" : "user",
            "content" : prompt
            }
        ],
        temperature = 0.7,
    )

    return response.choices[0].message.content