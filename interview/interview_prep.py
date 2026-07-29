import os
from dotenv import load_dotenv
from groq import Groq

# Load environment variables
load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found in the .env file.")

client = Groq(api_key=api_key)


def generate_questions(job_role, experience_level, skills, num_questions=10):
    prompt = f"""
You are a senior technical interviewer at a top technology company.

Generate exactly {num_questions} interview questions for the following candidate profile.

Job Role: {job_role}
Experience Level: {experience_level}
Skills: {skills}

Distribute the questions as follows:
- 50% Technical Questions
- 30% Behavioral Questions (start with "Tell me about a time when...")
- 20% Situational Questions (start with "What would you do if...")

For every question follow this format exactly:

Q[number]. Question

TYPE: Technical/Behavioral/Situational

DIFFICULTY: Easy/Medium/Hard

GOOD ANSWER: keyword1, keyword2, keyword3, keyword4

The questions should:
- Be specific to the given skills.
- Increase gradually from Easy to Hard.
- Avoid generic interview questions.
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "system",
                "content": f"""
You are an expert interviewer specializing in {job_role} roles.
Generate interview questions that resemble those asked by top technology companies.
"""
            },
            {
                "role": "user",
                "content": prompt
            }
        ],
        temperature=0.7
    )

    return response.choices[0].message.content


def evaluate_answer(question, answer, job_role):
    feedback_prompt = f"""
You are a senior interviewer hiring for a {job_role} role.

Interview Question:
{question}

Candidate Answer:
{answer}

Evaluate the answer and provide:

Score: X/10

Strengths:
- Point 1
- Point 2

Improvements:
- Point 1
- Point 2

Ideal Answer Summary:
(3-5 sentences)

Overall Verdict:
Excellent / Good / Average / Poor
"""

    response = client.chat.completions.create(
        model="llama-3.3-70b-versatile",
        messages=[
            {
                "role": "user",
                "content": feedback_prompt
            }
        ],
        temperature=0.5
    )

    return response.choices[0].message.content


def mock_interview(job_role):
    print("\n" + "=" * 60)
    print("MOCK INTERVIEW MODE")
    print("=" * 60)

    question = input("\nPaste one interview question:\n\n")

    print("\nTake your time and answer carefully.\n")

    answer = input("YOUR ANSWER:\n\n")

    if len(answer.strip()) < 20:
        print("\nAnswer is too short. Please provide a detailed response.")
        return

    print("\nEvaluating your answer...\n")

    feedback = evaluate_answer(question, answer, job_role)

    print("=" * 60)
    print("INTERVIEW FEEDBACK")
    print("=" * 60)
    print(feedback)


def main():
    print("=" * 60)
    print("🤖 AI INTERVIEW PREP TOOL")
    print("=" * 60)

    job_role = input("\nJob Role: ")

    experience_level = input(
        "Experience Level (Fresher/Junior/Mid/Senior): "
    )

    skills = input(
        "Skills (comma separated): "
    )

    num = input(
        "Number of Questions (Press Enter for 10): "
    ).strip()

    num_questions = int(num) if num else 10

    print("\nGenerating Interview Questions...\n")

    questions = generate_questions(
        job_role,
        experience_level,
        skills,
        num_questions
    )

    print("=" * 60)
    print("INTERVIEW QUESTIONS")
    print("=" * 60)

    print(questions)

    while True:
        choice = input(
            "\nDo you want to practice a question? (yes/no): "
        ).lower()

        if choice == "yes":
            mock_interview(job_role)

        elif choice == "no":
            print("\nThank you for using the AI Interview Prep Tool!")
            break

        else:
            print("Please enter yes or no.")


if __name__ == "__main__":
    main()