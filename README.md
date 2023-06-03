# ScrapeLogBTC
# Bitcoin Price Data Extraction using Web Scraping
This Python script utilizes web scraping techniques to extract Bitcoin price data from a specific webpage. It uses the Selenium library to automate a web browser, capturing screenshots and extracting information from the images using Optical Character Recognition (OCR).

# Dependencies
Selenium: A library for browser automation
time: For adding delays during the script execution
PIL: Python Imaging Library for image processing
pyautogui: Provides cross-platform mouse and keyboard control
io: For working with input and output streams
pytesseract: An OCR engine for extracting text from images
re: Regular expression library for text manipulation
pandas: A powerful data manipulation library

# Usage
The script initializes a Selenium WebDriver using Chrome and navigates to the target webpage.
It maximizes the browser window and scrolls down the page to ensure all relevant data is visible.
By simulating a mouse click, the script captures a screenshot of the webpage.
The screenshot is saved and opened using the Python Imaging Library (PIL).
The script then proceeds to locate a specific red line on the webpage, representing Bitcoin price data.
It extracts the price and date information by cropping and processing the relevant areas of the screenshot.
Optical Character Recognition (OCR) is performed using pytesseract to convert the image into text.
The extracted prices and dates are stored in lists.
The process is repeated for both the top and bottom parts of the webpage.
The extracted data is printed to the console and saved in an Excel file named "BTC.xlsx".

Please note that the code is designed to work with a specific webpage and assumes the presence of a red line indicating Bitcoin prices. Adjustments may be required for different webpages or data formats.

Feel free to customize and adapt the code to suit your specific needs.
