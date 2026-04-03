# 💼 Job Listings Scraper (Python)

A simple Python project I built to scrape job listings from a website, filter them by keyword, and save the results into a file.

I made this to practice web scraping and also to build something that feels a bit more real-world.

---

## 🚀 Features

- Search for jobs using a keyword  
- Limit how many results to return  
- Save results to a CSV file  
- Clean output in the terminal  

---

## 🛠️ Tech Used

- Python  
- requests  
- BeautifulSoup4  
- csv  

---

## ▶️ How to Run

```bash
git clone https://github.com/LynxCodez/job-scraper.git
cd job-scraper
pip install requests beautifulsoup4
python main.py
```

---
## 📂 Output

The script creates a jobs.csv file with:

- Job title
- Company
- Location

---

## 📚 What I Learned
- How to fetch and parse HTML using requests and BeautifulSoup
- How to loop through elements and extract specific data
- Ran into issues when some elements weren’t found, so I had to handle that properly
- Started organizing my code into functions instead of writing everything in one block

---

## 🔮 Future Improvements
- Add support for more job websites
- Improve error handling if the site structure changes
- Maybe turn this into a small web app later
- Add automatic scraping instead of running it manually

---

## 👨‍💻 Author

# LynxCodez

