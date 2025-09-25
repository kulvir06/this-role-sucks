#!/usr/bin/env python3
import ollama
import argparse
import sys

# Set up CLI arguments with flags
parser = argparse.ArgumentParser(description="Analyze resume against a job description using Ollama")
parser.add_argument("-resume", required=True, help="Path to the resume file")
parser.add_argument("-jd", required=True, help="Path to the job description file")
args = parser.parse_args()

# Read files
try:
    with open(args.resume, "r") as file:
        resume = file.read()
except FileNotFoundError:
    print(f"Error: Resume file '{args.resume}' not found.")
    sys.exit(1)

try:
    with open(args.jd, "r") as file:
        content = file.read()
except FileNotFoundError:
    print(f"Error: Job description file '{args.jd}' not found.")
    sys.exit(1)

# Prepare the prompt
ANALYZE_PROMPT = f"""
Act as an ATS screening process and analyze the resume.
The resume is as follows:
{resume}

Now, 
I am a masters' student in Computer Science and I am applying to get a summer internship at a company.
I want to tailor my resume in such a way that it has keywords that are listed in the job description of the company.
My goal is to pass the ATS screening process. 
I want you to act as an ATS screening process and tell me the keywords that I should include in my resume.

The job description is as follows:
{content}

The output should only be a list of keywords that are missing and I need to add them to my resume.
"""

# Call Ollama
response = ollama.chat(
    model="llama3.1:8b",
    messages=[{"role": "user", "content": ANALYZE_PROMPT}]
)

# Print results
print(response['message']['content'])