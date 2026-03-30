import requests
from bs4 import BeautifulSoup
import csv
import json
from datetime import datetime


BASE_URL = "https://realpython.github.io/fake-jobs/"


def fetch_page(url):
    """Fetch HTML content from a URL."""
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response.text
    except requests.exceptions.RequestException as error:
        print(f"[ERROR] Failed to fetch data: {error}")
        return None


def parse_jobs(html):
    """Extract job data from HTML."""
    soup = BeautifulSoup(html, "html.parser")
    job_cards = soup.find_all("div", class_="card-content")

    jobs = []
    for card in job_cards:
        job = {
            "title": card.find("h2", class_="title").text.strip(),
            "company": card.find("h3", class_="company").text.strip(),
            "location": card.find("p", class_="location").text.strip(),
        }
        jobs.append(job)

    return jobs


def filter_jobs(jobs, keyword, limit):
    """Filter jobs by keyword and limit results."""
    filtered = []

    for job in jobs:
        if keyword in job["title"].lower():
            filtered.append(job)

        if len(filtered) >= limit:
            break

    return filtered


def save_to_csv(jobs, filename="jobs.csv"):
    """Save job data to CSV file."""
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    with open(filename, mode="w", newline="", encoding="utf-8") as file:
        writer = csv.writer(file)
        writer.writerow(["Title", "Company", "Location", "Scraped At"])

        for job in jobs:
            writer.writerow([
                job["title"],
                job["company"],
                job["location"],
                timestamp
            ])


def save_to_json(jobs, filename="jobs.json"):
    """Save job data to JSON file."""
    with open(filename, "w", encoding="utf-8") as file:
        json.dump(jobs, file, indent=4)


def display_jobs(jobs):
    """Print jobs to console."""
    print(f"\nFound {len(jobs)} job(s)\n")

    for job in jobs:
        print(f"Title   : {job['title']}")
        print(f"Company : {job['company']}")
        print(f"Location: {job['location']}")
        print("-" * 40)


def main():
    """Main program execution."""
    print("=== Job Scraper ===")

    keyword = input("Enter job keyword: ").lower()
    limit = int(input("How many jobs do you want? "))

    html = fetch_page(BASE_URL)
    if not html:
        return

    jobs = parse_jobs(html)
    filtered_jobs = filter_jobs(jobs, keyword, limit)

    if not filtered_jobs:
        print("No jobs found.")
        return

    display_jobs(filtered_jobs)
    save_to_csv(filtered_jobs)
    save_to_json(filtered_jobs)

    print("\nData saved to jobs.csv and jobs.json")


if __name__ == "__main__":
    main()