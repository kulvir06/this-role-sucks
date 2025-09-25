import requests
from bs4 import BeautifulSoup
import urllib3
import warnings

# warnings.filterwarnings("ignore", category=UserWarning)

# urllib3.disable_warnings(urllib3.exceptions.InsecureRequestWarning)

def extract_job_description(url):
    try:
        # Send GET request
        # response = requests.get(url, headers={"User-Agent": "Mozilla/5.0"})
        response = requests.get(url)
        response.raise_for_status()  # raise error if status != 200

        # Parse HTML content
        soup = BeautifulSoup(response.text, "html.parser")

        # Remove script and style elements
        for script in soup(["script", "style"]):
            script.extract()

        # Get visible text
        text = soup.get_text(separator="\n")

        # Clean up whitespace
        lines = [line.strip() for line in text.splitlines() if line.strip()]
        clean_text = "\n".join(lines)

        return clean_text  # limit output length for readability

    except Exception as e:
        return f"Error: {e}"

# Example usage
url = "https://jobs.ea.com/en_US/careers/JobDetail/Online-Software-Engineer-Intern-SUMMER-2026/210918?utm_source=Simplify&ref=Simplify"
# url = "https://example.com/job-description"
# url = "https://jobs.smartrecruiters.com/ServiceNow/744000083003661?utm_source=Simplify&ref=Simplify"
# url = "https://oshkoshcorporation.wd5.myworkdayjobs.com/Oshkosh/job/Oshkosh-Wisconsin-United-States/Software-Display-intern_R41054?utm_source=Simplify&ref=Simplify"
# job_text = extract_job_description(url)
# print(job_text)