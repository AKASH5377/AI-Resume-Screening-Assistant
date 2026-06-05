import google.generativeai as genai

genai.configure(api_key="YOUR_API_KEY")

model = genai.GenerativeModel("gemini-pro")

resume = input("Paste Resume:\n")
job_description = input("\nPaste Job Description:\n")

prompt = f"""
Analyze the following resume against the job description.

Resume:
{resume}

Job Description:
{job_description}

Provide:
1. Match Score
2. Strengths
3. Missing Skills
4. Recommendation
"""

response = model.generate_content(prompt)

print(response.text)
