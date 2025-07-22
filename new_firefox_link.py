import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, StaleElementReferenceException

# Configuration
FIREFOX_PROFILE_PATH = r"C:\Users\alexuser\AppData\Roaming\Mozilla\Firefox\Profiles\9jrfrxn2.default-release"  # Path to Firefox user profile
FIREFOX_BINARY_PATH = r"C:\Program Files\Mozilla Firefox\firefox.exe"  # Path to Firefox binary
WEBDRIVER_PATH = r"C:\Users\alexuser\Downloads\alex\geckodriver.exe"  # Path to GeckoDriver
START_URL = "https://www.contractsfinder.service.gov.uk/Search/Results"
OUTPUT_FILE = "contract_links.xlsx"

# Set up Firefox options
options = webdriver.FirefoxOptions()
options.set_preference("profile", FIREFOX_PROFILE_PATH)  # Use the specific Firefox profile (optional)
#options.add_argument("--headless")  # Optional: run Firefox in headless mode
options.binary_location = FIREFOX_BINARY_PATH  # Specify the Firefox binary path

# Initialize WebDriver
service = Service(WEBDRIVER_PATH)
driver = webdriver.Firefox(service=service, options=options)

def wait_for_user_input():
    """
    Waits for the user to press Enter before proceeding.
    """
    input("Perform your search and apply filters. Press Enter when ready to scrape...")

def scrape_links():
    driver.get(START_URL)
    all_links = []
    page_count = 1
    max_retries = 3

    # Wait for user input before scraping
    wait_for_user_input()

    try:
        while page_count <= 556:
            retries = 0
            while retries < max_retries:
                try:
                    # Wait for links to load
                    WebDriverWait(driver, 30).until(
                        EC.presence_of_element_located((By.CSS_SELECTOR, "[id^='dashboard_notices'] a.govuk-link.search-result-rwh"))
                    )
                    break
                except TimeoutException:
                    retries += 1
                    print(f"Timeout occurred, retrying ({retries}/{max_retries})")
                    if retries == max_retries:
                        print("Max retries reached, exiting...")
                        return
                    driver.refresh()
                    time.sleep(5)

            # Extract links with handling of StaleElementReferenceException
            links = []
            try:
                link_elements = driver.find_elements(By.CSS_SELECTOR, "[id^='dashboard_notices'] a.govuk-link.search-result-rwh")
                for link in link_elements:
                    links.append(link.get_attribute('href'))
            except StaleElementReferenceException:
                print("A stale element was encountered, re-fetching links...")
                link_elements = driver.find_elements(By.CSS_SELECTOR, "[id^='dashboard_notices'] a.govuk-link.search-result-rwh")
                for link in link_elements:
                    links.append(link.get_attribute('href'))

            # Add links to the list
            for link in links:
                all_links.append(link)
            print(f"Page {page_count}: Collected {len(links)} links")

            # Save progress periodically
            if page_count % 10 == 0:
                save_to_excel(all_links)
                print(f"Saved interim progress at page {page_count}")

            # Handle next page
            try:
                next_button = WebDriverWait(driver, 20).until(
                    EC.element_to_be_clickable((By.CSS_SELECTOR, "li.standard-paginate-next-box a.standard-paginate-next"))
                )
                next_button.click()
                page_count += 1
                # Wait for page to load
                time.sleep(2)
            except (TimeoutException, NoSuchElementException):
                print("No more pages found")
                break

    finally:
        save_to_excel(all_links)
        driver.quit()

def save_to_excel(links):
    df = pd.DataFrame(links, columns=["Links"])
    df.to_excel(OUTPUT_FILE, index=False)
    print(f"Saved {len(links)} links to {OUTPUT_FILE}")

if __name__ == "__main__":
    scrape_links()
    print("Scraping completed successfully!")
