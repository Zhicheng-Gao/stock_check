# TechFast Product Stock Monitor & Email Notifier

This Python script uses Selenium to automatically monitor the stock status of a product on [TechFast](https://ozb.techfast.com.au). Once the product is detected as "In Stock", the script will immediately send you an email notification via Gmail.

## 🔍 Features

- Automatically opens the product page and checks stock status
- Runs in headless mode (no visible browser window)
- Sends an email alert once the product is available
- Checks stock status every minute until stock is found
- Tracks and prints the number of check attempts
- Saves a screenshot (`not_found.png`) if the "Add to Cart" button is not found

## 🛠️ Installation

Install required Python packages:

```bash
pip install selenium
```

You must also install [Google Chrome](https://www.google.com/chrome/) and the matching version of [ChromeDriver](https://sites.google.com/chromium.org/driver/). Ensure `chromedriver` is either in your system PATH or in the same folder as your script.

## ✉️ Gmail Setup

1. Go to your Gmail account settings → **Security**
2. Enable **2-Step Verification**
3. Create an **App Password**
4. Paste the generated app password (without spaces) into the `EMAIL_PASSWORD` variable in the script

## 🚀 How to Use

1. Update the following variables in the script:
   - `EMAIL_SENDER`: Your Gmail address
   - `EMAIL_PASSWORD`: Your Gmail App Password
   - `EMAIL_RECEIVER`: The email to receive notifications (can be your own)
   - `URL`: The product URL you want to monitor
2. Run the script:

```bash
python check_stock.py
```

1. The terminal will print a status message every minute. If stock is found, the script will send an email and exit.

## ✅ Sample Output

```
🕵️ Attempt 5 to check stock...
✅ Found Add to Cart button, trying to click...
✅ Product is in stock!
✅ Email sent successfully!
🎉 Notification sent, ending monitoring.
```

## 📷 Screenshot on Error

If the "Add to Cart" button cannot be found, the script will save a screenshot as `not_found.png` for debugging (e.g., if the page structure changes).

## ⚠️ Notes

- Avoid setting the check interval too short (recommend ≥30 seconds) to reduce the risk of IP bans or unnecessary server load.
- If TechFast changes its website layout or button class names, you may need to update the logic in the `check_stock()` function.

------

Made with ❤️ for deal hunters & automation fans.
