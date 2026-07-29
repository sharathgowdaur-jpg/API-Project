# 🎯 AI Interview Question Generator

An AI-powered Interview Question Generator built using **Python** and the **Groq API**. It generates technical, behavioral, and situational interview questions based on the user's job role, experience level, and skills.

---

## 🚀 Features

- Generate AI-powered interview questions
- Technical, Behavioral, and Situational questions
- Adjustable difficulty (Easy → Medium → Hard)
- Uses Groq LLM (Llama 3.3 70B)
- Environment variable support using `.env`

---

## 📂 Project Structure

```
interview/
│── interview_prep.py
│── .env
│── requirements.txt
│── README.md
```

---

# 🛠 Prerequisites

- Python 3.10+
- Groq API Key

---

# ⚙️ Installation

## 1. Clone the repository

```bash
git clone <your_repository_url>
cd interview
```

---

## 2. Create a Virtual Environment

### Windows

```bash
python -m venv venv
```

Activate it

```bash
venv\Scripts\activate
```

### Linux / macOS

```bash
python3 -m venv venv
source venv/bin/activate
```

---

## 3. Upgrade pip

```bash
python -m pip install --upgrade pip
```

---

## 4. Install Dependencies

```bash
pip install groq
pip install python-dotenv
```

Or install everything together

```bash
pip install groq python-dotenv
```

---

## 5. Create a `.env` file

Create a file named

```
.env
```

Add your Groq API key

```env
GROQ_API_KEY=gsk_your_api_key_here
```

---

## 6. Load API Key

```python
load_dotenv()

client = Groq(
    api_key=os.getenv("GROQ_API_KEY")
)
```

---

# ▶️ Running the Project

```bash
python interview_prep.py
```

---

# 📦 requirements.txt

Create a file named

```
requirements.txt
```

Add

```
groq
python-dotenv
```

Install later using

```bash
pip install -r requirements.txt
```

---

# 🔑 Get a Groq API Key

1. Visit

https://console.groq.com/

2. Login

3. Create an API Key

4. Copy it into the `.env` file

---

# 💻 Example

```python
questions = generate_function(
    job_role="Python Developer",
    experience_level="Fresher",
    skills="Python, OOP, SQL",
    num_questions=10
)

print(questions)
```

---

# 🛠 Troubleshooting

## ModuleNotFoundError: No module named 'dotenv'

Install

```bash
pip install python-dotenv
```

---

## ModuleNotFoundError: No module named 'groq'

Install

```bash
pip install groq
```

---

## API Key Not Found

Check your `.env` file

```env
GROQ_API_KEY=gsk_xxxxxxxxxxxxxxxxxxxxx
```

---

## Virtual Environment

Activate before running

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

---

# 📚 Technologies Used

- Python
- Groq API
- Llama 3.3 70B Versatile
- python-dotenv

---

# 📄 License

This project is licensed under the MIT License.

---

## 👨‍💻 Author

Sharath U R
