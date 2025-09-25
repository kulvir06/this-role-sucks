import ollama

from extract import extract_job_description

content = ""
with open("plaintext.txt", "r") as file:
    content = file.read()

print(content)
# simple keyword extraction example
url = "https://bostonscientific.eightfold.ai/careers/job/563602808714251?utm_source=Simplify&ref=Simplify"
# url = "https://jobs.ea.com/en_US/careers/JobDetail/Online-Software-Engineer-Intern-SUMMER-2026/210918?utm_source=Simplify&ref=Simplify"
# url = "https://example.com/job-description"
# url = "https://jobs.smartrecruiters.com/ServiceNow/744000083003661?utm_source=Simplify&ref=Simplify"
# url = "https://oshkoshcorporation.wd5.myworkdayjobs.com/Oshkosh/job/Oshkosh-Wisconsin-United-States/Software-Display-intern_R41054?utm_source=Simplify&ref=Simplify"
# job_text = extract_job_description(url)
# print(job_text)
# prompt = f"""
# You are an expert recruiter. Extract keywords from the text below.
# Output ONLY valid JSON with arrays: skills, tools, certifications, roles, soft_skills, keywords.
# include any keywords from the company description or job requirements in the `skills` and `roles` arrays

# TEXT:
# {content}
# """

PROMPT = """
I am a masters' student in Computer Science and I am applying to get a summer internship at a company.
I want to tailor my resume in such a way that it has keywords that are listed in the job description of the company.
My goal is to pass the ATS screening process. 
I want you to act as an ATS screening process and tell me the keywords that I should include in my resume.
The output should be a list of keywords.
The job description is as follows:
{content}
"""

prompt = PROMPT.format(content=content)
response = ollama.chat(
    model="llama3.1:8b",   # or vicuna, mistral, etc.
    messages=[{"role": "user", "content": prompt}]
)

print(response['message']['content'])


