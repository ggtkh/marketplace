from playwright.sync_api import Page, sync_playwright
from urllib.parse import quote
from time import sleep

def get_a_good(good_name):
    encoded_name = quote(good_name)
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        page = browser.new_page()
        page.goto(f"https://www.google.com/search?q={encoded_name}")
        print(encoded_name)
        input('a')


get_a_good("Склянки")