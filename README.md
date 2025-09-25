# this-role-sucks

This tool helps you analyse a job description and your resume and using OLLAMA it suggests missing **keywords** to help tailor your resume to pass Applicant Tracking Systems (ATS).

---

## 🚀 Quick Start

### Clone the Repository
```bash
git clone https://github.com/yourusername/this-role-sucks.git
cd this-role-sucks
```

### Prerequisites
- Python 3.8+
- Ollama installed and running

📋 **Need help with installation?** → [See detailed installation guide](INSTALLATION.md)

### Run the Tool

```bash
python cli.py -resume resume.txt -jd job_description.txt
python3 cli.py -resume resume.txt -jd job_description.txt
```

**Command Arguments:**
- `-resume`: Path to your resume file (text format)
- `-jd`: Path to the job description file (text format)

### Example Output
The tool will analyze your resume against the job description and output a list of missing keywords that you should add to your resume to improve ATS compatibility.


## 🔧 Quick Troubleshooting

**Ollama not running?**
```bash
ollama serve
```

**Model not found?**
```bash
ollama pull llama3.1:8b
```

**Need complete setup?** → [See installation guide](INSTALLATION.md)