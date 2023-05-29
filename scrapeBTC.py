from selenium import webdriver
import time as t
from PIL import Image
import pyautogui
import io
import pytesseract
import re
import pandas as pd

url = "https://www.btcgoto.com/bitcoin/regression-bands"

webdriver = webdriver.Chrome()
webdriver.get(url)
webdriver.maximize_window()
webdriver.execute_script("window.scrollBy(0, 1000)")
t.sleep(1)
pyautogui.click(x=1572, y=938)
screenshot = webdriver.get_screenshot_as_png()
webdriver.save_screenshot('screenshot.png')
image = Image.open(io.BytesIO(screenshot))

red_pixel = (192, 0, 0, 255)  # define the RGB color of the red line


def BTC_prices_dates(top_or_bot):
    coords = []
    for x in range(image.width):
        for y in range(image.height)[::top_or_bot]:
            pixel = image.getpixel((x, y))
            if pixel == red_pixel and y < 800 and x > 1517:
                red_x = x
                red_y = y
                coords.append((red_x, red_y))
                break

    prices = []
    dates = []
    for (i, j) in coords:
        pyautogui.moveTo(i, j + 45)

        screenshot1 = webdriver.get_screenshot_as_png()
        image1 = Image.open(io.BytesIO(screenshot1))
        img_price = image1.crop((0, j - 9, 56, j + 8))
        img_date = image1.crop((i - 40, 959, i + 39, 977))

        # image1.show()
        # price.show()
        # date.show()

        price = re.sub(r'[^a-zA-Z0-9]', '', pytesseract.image_to_string(img_price))
        print(price)
        date = re.sub(r'[^a-zA-Z0-9]', '', pytesseract.image_to_string(img_date))
        print(date)
        prices.append(price)
        dates.append(date)
    return prices, dates

top_prices, top_dates = BTC_prices_dates(1)
print(top_prices)
print(top_dates)

bot_prices, bot_dates = BTC_prices_dates(-1)
print(bot_prices)
print(bot_dates)
df = pd.DataFrame(bot_dates, columns=['bot_dates'])
df['bot_prices'] = bot_prices
df['top_dates'] = bot_dates
df['top_prices'] = top_prices

df.to_excel('BTC.xlsx', index=False, sheet_name='Sheet1')

