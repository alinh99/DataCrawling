# ⚽ Football Club Data Crawler (Python)
## 📖 Overview
This project is a **data crawling system** designed to collect football club data from a public website by city. It began as a **Selenium-based web crawler (v1)** and later evolved into a **fully optimized asynchronous API crawler (v2)** for higher performance, scalability, and stability.
## ⚙️ Technologies
- **Python 3.9+**
- **Selenium (v1)**
- **Asyncio + httpx (v2)**
- **Multiprocessing + AsyncIO hybrid execution**
- **Adaptive concurrency limiter**
- **Pickle-based caching & checkpoint recovery**
- **Retry logic & backoff strategy**
- **Logging + tqdm progress bar**

## 🧩 Project Structure
football_club_crawling/
│
├── city_crawling.py # Step 1: Crawl city list
├── club_crawling_v1.py # Step 2 (Version 1): Selenium crawler
├── club_crawling_v2.py # Step 2 (Version 2): Async + API crawler
│
├── requirements_v1.txt # Dependencies for v1
├── requirements_v2.txt # Dependencies for v2
│
├── .env # Environment variables (API base URL, output path, etc.)
├── logs/ # Folder for runtime logs
├── data/ # Folder for city lists, output CSV
├── storage/ # Folder for cache files (mostly pkl files)
└── README.md # Project documentation

## 🧠 Conceptual Flow
1. **`city_crawling.py`** — Collects all available cities that contain football clubs and saves them as a CSV or list file.  
2. **`club_crawling_v1.py`** (Selenium-based) — Opens the browser, loads each city page, and extracts club data (names, age groups, types, etc.).  
3. **`club_crawling_v2.py`** (Async + API-based) — Uses API endpoints directly with asynchronous HTTP requests to crawl data **in parallel**, while maintaining server stability using **adaptive rate control** and retry logic.

## 🚀 Setup
### 🧰 1. Install Python
Install Python 3.9 or above: [https://www.python.org/downloads/](https://www.python.org/downloads/)
### ⚙️ 2. Install Dependencies
#### 🧩 For Version 1 (Selenium-based)
```
pip install -r requirements_v1.txt
```
#### ⚡ For Version 2 (Async + API-based)
- **On Windows:**
```
pip install -r requirements_v2.txt
```
- **On Linux/macOS (Recommended for max performance):**
```
pip install -r requirements_v2.txt
```
```
pip install uvloop
```
> ⚠️ Note: `uvloop` cannot be installed on Windows but can **boost async performance by 30–50%** on Linux/macOS.

### 🧾 Example `.env` File
```
API_CLUB_RECOMMENDATION_URL = "https://example.com/api"
API_CLUB_INFO_URL = "https://example.com/api"
KEY_CLUB_INFO_AND_RECOMMENDATION_INFO =  ""
KEY_CLUB_CONTACT_INFO = ""
WEBSITE_URL = "https://find.englandfootball.com/"
WEBSITE_NAME = "EnglandFootballClub"
MAX_PROCESSES = 5
MAX_CONCURRENT_REQUESTS = 10000000000
BATCH_SAVE_SIZE = 200
RATE_LIMIT_SLEEP = 60
```

### 🧩 Step 2A — Crawl Clubs Using Selenium (v1)
```
python city_crawling.py
```
### 🧩 Step 2A — Crawl Clubs Using Selenium (v1)
```
Output: `data/clubs_data.csv`
```
Output: `data/clubs_data.csv`

## 📊 Comparison: Version 1 vs Version 2
| Feature / Aspect | v1 — Selenium Version | v2 — Async API Version |
|------------------|------------------------|-------------------------|
| **Core Technology** | Selenium (browser automation) | Asyncio + httpx (API requests) |
| **Speed** | 🐢 Slow — one browser per page | ⚡ Extremely fast — async + multiprocessing |
| **Performance Control** | None | Adaptive limiter + retry with exponential backoff |
| **System Resource Usage** | High (multiple browsers open) | Low (non-blocking I/O) |
| **Stability** | Can crash or hang | Stable with caching and automatic retries |
| **Error Recovery** | Manual restart | Auto resume from cache and pickle checkpoints |
| **Use Case** | Prototype / small dataset | Large-scale / production-grade crawling |
| **Compatibility** | Works on all OS | Best on Linux/macOS (uvloop supported) |
## 🧩 Requirements Summary
### `requirements_v2.txt`

*(Optional for Linux/macOS only)*
```
pip install uvloop
```

## 🎯 Learning & Technical Takeaways
| Concept | Description |
|----------|-------------|
| **Asynchronous Programming (asyncio)** | Handles thousands of requests concurrently without blocking. |
| **Multiprocessing** | Runs multiple cities in parallel using CPU cores. |
| **Adaptive Rate Limiting** | Adjusts speed automatically when the target server slows down. |
| **Pickle Caching** | Saves progress and skips duplicates. |
| **Retry & Error Handling** | Retries failed requests with exponential backoff. |
| **Logging & tqdm** | Real-time progress tracking. |

## 🏁 Author
**Linh Nguyen Hoang**  
🎯 Aspiring Python Backend / Data Engineer
🌍 Goal: Build a high-performance asynchronous crawler to collect and process structured football club data efficiently.
📧 Contact: *[alinh1803@gmail.com]*  
## 📜 License
MIT License © 2025 Linh Nguyen Hoang