# Installation Guide

This guide provides detailed installation instructions for all operating systems.

---

## 🚀 Prerequisites

- Python 3.8+
- [Ollama](https://ollama.com/) installed on your system

---

## ⚙️ Installation & Setup

### 1. Install Python Dependencies

First, install the required Python package:

```bash
pip install ollama
```

### 2. Install Ollama

#### macOS
**Option 1: Using Homebrew (Recommended)**
```bash
brew install ollama
```

**Option 2: Direct Download**
1. Visit [https://ollama.com/download](https://ollama.com/download)
2. Download the macOS installer
3. Run the installer

#### Windows
**Option 1: Using Chocolatey**
```bash
choco install ollama
```

**Option 2: Direct Download**
1. Visit [https://ollama.com/download](https://ollama.com/download)
2. Download the Windows installer
3. Run the installer

#### Linux
**Using curl (Recommended)**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

**Using apt (Ubuntu/Debian)**
```bash
# Add Ollama repository
curl -fsSL https://ollama.com/install.sh | sh
```

**Using yum/dnf (CentOS/RHEL/Fedora)**
```bash
curl -fsSL https://ollama.com/install.sh | sh
```

### 3. Start Ollama Service

Start the Ollama service in the background:

```bash
ollama serve
```

### 4. Download Required Model

After starting Ollama, download the Llama 3.1 model.
Go to a new terminal window and execute the following command:

```bash
ollama pull llama3.1:8b
```

---

## 🔧 Complete Setup Sequence

If you're setting up for the first time, run these commands in order:

```bash
# 1. Install Python dependencies
pip install ollama

# 2. Start Ollama service
ollama serve

# 3. Download the required model (in a new terminal)
ollama pull llama3.1:8b

# 4. Run the tool
python cli.py -resume resume.txt -jd job_description.txt
```

---

## 🏃‍♂️ How to Run

### Basic Usage

```bash
python cli.py -resume <path_to_resume_file> -jd <path_to_job_description_file>
```

### Example

```bash
python cli.py -resume resume.txt -jd job_description.txt
```

### Command Line Arguments

- `-resume`: **Required** - Path to your resume file (text format)
- `-jd`: **Required** - Path to the job description file (text format)

### Output

The tool will analyze your resume against the job description and output a list of missing keywords that you should add to your resume to improve ATS compatibility.

---

## 📝 File Format

Both resume and job description files should be in plain text format (.txt). The tool will read the content and analyze it using the Ollama Llama 3.1 model.

---

## 🔧 Troubleshooting

### Ollama not running
Make sure Ollama is running in the background:
```bash
ollama serve
```

### Model not found
If you get a model error, ensure the model is downloaded:
```bash
ollama pull llama3.1:8b
```

### File not found errors
Make sure the file paths are correct and the files exist in the specified locations.

---

## 📚 Additional Resources

- [Ollama Official Documentation](https://ollama.com/)
- [Llama 3.1 Model Information](https://ollama.com/library/llama3.1)
