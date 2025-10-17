# ⚽ Football Club Data Crawler (Python)
## 📖 Overview
This project is a **data crawling system** that collects **football club information** from **public web sources** by city.  
It started as a **basic Selenium-based crawler (v1)**, was enhanced with **multi-browser parallelism** for better efficiency (**v2**),  
and ultimately evolved into an **asynchronous API-powered crawler (v3)** — achieving **high performance ⚡**, **scalability 🌍**, and **production-level stability 🧩**.

## ⚙️ Technologies
- **Python 3.9+**
- **Selenium (v1)** — Browser automation for crawling web content
- **Selenium + Threading (v2)** — Multi-browser concurrent crawling for higher throughput
- **Asyncio + httpx (v3)** — Fully asynchronous API request–based crawler
- **Multiprocessing + AsyncIO hybrid execution**
- **Adaptive concurrency limiter** to balance performance and server stability
- **Pickle-based caching & checkpoint recovery** for safe resume after interruptions
- **Retry logic & exponential backoff** for network stability
- **Logging system + tqdm progress bar** for real-time monitoring
---

## 🧩 Project Structure
`````
FootballClubDataCrawler/
│
├── city_crawling.py # Step 1: Crawl city list
│
├── club_crawling_v1.py # Step 2 (Version 1): Basic Selenium crawler
├── club_crawling_v2.py # Step 2 (Version 2): Optimized Selenium + multi-browser
├── club_crawling_v3.py # Step 2 (Version 3): Async + API-based high-performance crawler
│
├── requirements_v1_v2.txt # Dependencies for v1
├── requirements_v1_v2.txt # Dependencies for v2 (Selenium optimized)
├── requirements_v3.txt # Dependencies for v3 (Async API version)
│
├── .env # Environment variables (API base URL, output path, etc.)
├── logs/ # Folder for runtime logs
├── data/ # Folder for city lists, output CSV files
├── storage/ # Folder for cache files (pickle, checkpoints)
└── README.md # Project documentation
`````
## 🧠 Conceptual Flow
1. **`city_crawling.py`** — Collects all available cities that contain football clubs and saves them as a CSV or list file.  
2. **`club_crawling_v1.py`** (Selenium) — Opens the browser, loads each city page, and extracts club data (names, age groups, types, etc.), but **highly optimized** for better performance and reliability compared to early versions..
3. **`club_crawling_v2.py`** (Selenium) — Opens the browser, loads each city page, and extracts club data (names, age groups, types, etc.).
4. **`club_crawling_v3.py`** (Async + API-based) — Uses API endpoints directly with asynchronous HTTP requests to crawl data **in parallel**, while maintaining server stability using **adaptive rate control** and retry logic.

## 🚀 Setup
### 🧰 1. Install Python
Install Python 3.9 or above: [https://www.python.org/downloads/](https://www.python.org/downloads/)
### ⚙️ 2. Install Dependencies
#### 🧩 For Version 1 (Selenium)
```
pip install -r requirements_v1_v2.txt
```
#### 🧩 For Version 2 (Selenium)
```
pip install -r requirements_v1_v2.txt
```
#### ⚡ For Version 3 (Async + API-based)
- **On Windows:**
```
pip install -r requirements_v3.txt
```
- **On Linux/macOS (Recommended for max performance):**
```
pip install -r requirements_v3.txt
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

## 🧩 Version Comparison

| Feature / Aspect | v1 — Basic Selenium | v2 — Optimized Selenium (Multi-Browser) | v3 — Async API Request |
|------------------|---------------------|------------------------------------------|-------------------------|
| **Core Technology** | Selenium WebDriver | Selenium (parallel multi-browser) | Asyncio + HTTPX (direct API requests) |
| **Speed** | 🐢 Slow — single browser, sequential | ⚙️ Moderate — faster with parallel threads | ⚡ Extremely fast — async + connection pooling |
| **Performance Control** | None | Limited concurrency tuning | Adaptive limiter + retry with exponential backoff |
| **System Resource Usage** | Very high (1 browser per thread) | High (multi-browser consumes more CPU/RAM) | Low (non-blocking I/O, lightweight) |
| **Stability** | Prone to crashes or freezes | Improved but still limited by browser instability | Highly stable with caching & auto retries |
| **Error Recovery** | Manual rerun required | Partial recovery via logging | Full auto-resume using cache & pickle checkpoints |
| **Maintainability** | Simple but inefficient | More complex with multi-thread setup | Clean structure, easier to scale or integrate |
| **Scalability** | Poor — limited by Selenium overhead | Moderate — improved via concurrency | Excellent — supports distributed crawling |
| **Use Case** | Prototype / testing phase | Medium-scale crawling | Production-grade large-scale crawling |
| **Compatibility** | Works on all OS | Works on all OS | Best on Linux/macOS (with `uvloop` optimization) |


## 🧩 Requirements Summary
### `requirements_v3.txt`

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