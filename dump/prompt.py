PROMPT = """
I am a masters' student in Computer Science and I am applying to get a summer internship at a company.
I want to tailor my resume in such a way that it has keywords that are listed in the job description of the company.
My goal is to pass the ATS screening process. 
I want you to act as an ATS screening process and tell me the keywords that I should include in my resume.
The output should be a list of keywords.
The job description is as follows:
{content}
"""

ANALYZE_PROMPT = """
Act as an ATS screening process and analyze the resume.
The resume is as follows:
{resume}
"""