from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.common.exceptions import NoSuchElementException
import time
import smtplib
from email.mime.text import MIMEText

# Email Configuration
SMTP_SERVER = "smtp.gmail.com"
SMTP_PORT = 587
EMAIL_SENDER = "xxx@gmail.com"           # Your Gmail address
EMAIL_PASSWORD = "xxxx xxxx xxxx xxxx".replace(" ", "")  # Your app-specific password
EMAIL_RECEIVER = "xxx@gmail.com"         # Receiver is also yourself

# Page URL
URL = "https://ozb.techfast.com.au/products/xxx"

def send_email():
    msg = MIMEText(f"🎉 In Stock! Place your order quickly!\n\nLink: {URL}")
    msg["Subject"] = "[Stock Alert] TechFast XXX"
    msg["From"] = EMAIL_SENDER
    msg["To"] = EMAIL_RECEIVER

    with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
        server.starttls()
        server.login(EMAIL_SENDER, EMAIL_PASSWORD)
        server.send_message(msg)
        print("✅ Email alert sent!")

def check_stock():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--disable-gpu")
    options.add_argument("--log-level=3")

    driver = webdriver.Chrome(options=options)
    driver.get(URL)
    time.sleep(3)

    try:
        # Precisely locate the div button using class name 'AddOrange'
        add_to_cart = driver.find_element(By.CLASS_NAME, "AddOrange")
        print("✅ Found 'Add to Cart' button, attempting to click...")
        driver.execute_script("arguments[0].click();", add_to_cart)
        time.sleep(3)

        # Get page text content, check if it contains "Out of Stock"
        body_text = driver.page_source.lower()
        if "out of stock" in body_text:
            print("❌ Currently out of stock")
            result = False
        else:
            print("✅ Detected in stock!")
            result = True

    except NoSuchElementException:
        print("⚠️ 'Add to Cart' button not found")
        driver.save_screenshot("not_found.png")
        result = False

    driver.quit()
    return result

if __name__ == "__main__":
    attempt = 1  # Initialize check count

    while True:
        print(f"\n\n🕵️ Checking stock, attempt {attempt}...")
        try:
            if check_stock():
                send_email()
                print("🎉 Email notification sent, ending monitoring.")
                break
        except Exception as e:
            print(f"An error occurred: {e}")

        attempt += 1
        time.sleep(60)  # Check every 1 minute