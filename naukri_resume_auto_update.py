from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import os

# ✅ Replace with your actual info
EMAIL = "your_email@example.com"
PASSWORD = "p@ssw0rd"
CHROMEDRIVER_PATH = "C:\\WebDriver\\chromedriver.exe"
RESUME_FILE_PATH = "C:\\NaukriResume\\resume_updated.pdf"  # Update with your resume file path
# Make sure to have the correct path to your chromedriver executable and resume file

def login(driver):
    print("🔓 Opening Naukri login page...")
    driver.get("https://www.naukri.com/nlogin/login")
    wait = WebDriverWait(driver, 5)

    wait.until(EC.presence_of_element_located((By.ID, "usernameField"))).send_keys(EMAIL)
    driver.find_element(By.ID, "passwordField").send_keys(PASSWORD + Keys.RETURN)
    print("✅ Logged in.")
    time.sleep(5)

    # Try clicking 'View profile' if exists
    try:
        view_profile = WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "//a[text()='View profile']"))
        )
        print("👆 Clicking 'View profile'...")
        view_profile.click()
    except:
        print("⚠ 'View profile' button not found, manually going to profile page...")
        driver.get("https://www.naukri.com/mnjuser/profile")

def upload_resume(driver):
    wait = WebDriverWait(driver, 5)

    print("🌐 Waiting for resume section to load...")
    update_btn = wait.until(EC.element_to_be_clickable((By.XPATH, "//input[@type='button' and @value='Update resume']")))
    update_btn.click()


    print("📂 Uploading resume file...")
    file_input = wait.until(EC.presence_of_element_located((By.XPATH, "//input[@type='file']")))
    
    if os.path.exists(RESUME_FILE_PATH):
        file_input.send_keys(RESUME_FILE_PATH)
        print("⏳ Waiting for upload to complete...")
        time.sleep(6)
        print("✅ Resume uploaded successfully!")
    else:
        print("❌ Resume file not found at:", RESUME_FILE_PATH)

def main():
    chrome_options = Options()
    chrome_options.add_argument("--disable-notifications")
    chrome_options.add_argument("--start-maximized")

    driver = webdriver.Chrome(service=Service(CHROMEDRIVER_PATH), options=chrome_options)

    try:
        login(driver)
        upload_resume(driver)
    finally:
        print("🚪 Closing browser.")
        driver.quit()

if __name__ == "__main__":
    main()