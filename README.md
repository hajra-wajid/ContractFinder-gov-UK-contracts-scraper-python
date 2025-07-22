# ContractFinder-gov-UK-contracts-scraper-python
A robust Python web scraper using Python and Selenium to extract over 392,806 government contract records from official procurement portals. Designed to handle diverse website structures and deliver clean, structured data for market analysis and competitive intelligence.
<br>
# Government Contracts Data Scraper

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![Scrapy](https://img.shields.io/badge/Scrapy-2.x-green.svg)
![Playwright](https://img.shields.io/badge/Playwright-1.x-orange.svg)

## Project Overview

This repository contains a robust and scalable web scraping solution developed in Python to extract comprehensive government contract data from various official procurement portals. The system is designed to efficiently collect over 392,806 contract records, including details such as Title, Buyer, Industry, Location, Value, Dates, Description, and Supplier information.

## Key Features

-   **High-Volume Data Extraction:** Capable of extracting hundreds of thousands of records from diverse government websites.
-   **Adaptable Scraping:** Handles varied website layouts, JavaScript-heavy pages, and anti-bot measures using Scrapy and Playwright.
-   **Comprehensive Data Fields:** Extracts a wide array of specific contract details for in-depth analysis.
-   **Structured Data Output:** Delivers clean, organized data in CSV format, ready for direct import into databases or analytical tools.
-   **Scalable Architecture:** Built for efficiency and reliability across numerous procurement portals.

## Technologies Used

-   **Python 3.x**
-   **Scrapy 2.x**
-   **Playwright 1.x**
-   **Pandas** (for data processing and structuring)

## Installation

1.  **Clone the repository:**
    ```bash
    git clone https://github.com/hajra-wajid/gov-contracts-scraper-python.git
    cd gov-contracts-scraper-python
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    source venv/bin/activate  # On Windows: `venv\Scripts\activate`
    ```

3.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

    _Note: A `requirements.txt` file will be provided in the actual repository containing `scrapy`, `playwright`, `pandas`._

4.  **Install Playwright browsers:**
    ```bash
    playwright install
    ```

## Usage

1.  **Configure your scraper:**
    Open `settings.py` (if using Scrapy) or the main Python script and adjust any necessary settings (e.g., `DOWNLOAD_DELAY`, `USER_AGENT`, `CONCURRENT_REQUESTS`).

2.  **Run the scraper:**
    ```bash
    scrapy crawl gov_contracts_spider -o gov_contracts_data.csv
    ```
    (Replace `gov_contracts_spider` with the actual name of your Scrapy spider if different, or execute your main Python script directly.)

## Data Output

The extracted data will be saved in `gov_contracts_data.csv` (or your specified output file) with columns such as:

-   `Title`
-   `Buyer`
-   `Industry`
-   `Location of contract`
-   `Value of contract`
-   `Procurement reference`
-   `Published date`
-   `Closing date`
-   `Closing time`
-   `Contract start date`
-   `Contract end date`
-   `Contract type`
-   `Procedure type`
-   `Contract is suitable for SMEs?`
-   `Contract is suitable for VCSEs?`
-   `Description`
-   `Awarded date`
-   `Buyer Contact name`
-   `Buyer Address`
-   `Buyer Email`
-   `Supplier`
-   `Supplier Address`
-   `Reference`

## Contributing

Contributions are welcome! Please feel free to open issues or submit pull requests.

## Contact

For any questions or collaborations, feel free to reach out:

-   **Upwork Profile:** [https://www.upwork.com/freelancers/hajrawajid?mp_source=share](https://www.upwork.com/freelancers/hajrawajid?mp_source=share)
-   **GitHub Profile:** [https://github.com/hajra-wajid](https://github.com/hajra-wajid)
