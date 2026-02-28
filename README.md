# Code Alpha Internship – Task 1  
## Web Scraping Using Python

### 📌 Project Overview
This project was completed as part of my **Alpha Internship – Task 1**.

The objective of this task was to perform web scraping using Python and extract book details from the website:

http://books.toscrape.com/

The extracted data includes:
- 📖 Book Title  
- 💰 Price (converted from British Pounds to Indian Rupees ₹)  
- ⭐ Rating  
- 📦 Availability  

The collected data is cleaned, structured, and stored in a CSV file for further analysis.

---

### 🛠️ Technologies Used
- Python  
- Requests  
- BeautifulSoup (bs4)  
- Pandas  

---

### ⚙️ Project Workflow
1. Sent an HTTP request to the website using the Requests library.  
2. Parsed the HTML content using BeautifulSoup.  
3. Extracted book title, price, rating, and availability information.  
4. Converted the price from Pound (£) to INR (₹) using a fixed conversion rate.  
5. Stored the extracted data in a Pandas DataFrame.  
6. Exported the final dataset to a CSV file (`books_data_inr.csv`).  

---

### 📁 Project Files
- `web_scraping.py` – Python script used for web scraping  
- `books_data_inr.csv` – Output file containing the scraped data  
- `README.md` – Project documentation  

---

### ▶️ How to Run

Install the required libraries:

```bash
pip install requests beautifulsoup4 pandas
```

Run the script:

```bash
python web_scraping.py
```

---

### 🎯 Learning Outcomes
- Gained practical experience in web scraping  
- Learned HTML parsing using BeautifulSoup  
- Performed data cleaning and transformation  
- Exported structured data using Pandas  

---

✅ Successfully completed Alpha Internship – Task 1.
