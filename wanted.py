from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup

p = sync_playwright().start()

# browser = p.chromium.launch()
browser = p.chromium.launch(headless=False)

page = browser.new_page()

page.goto("https://www.wanted.co.kr/")
time.sleep(2)

page.click("button.Aside_searchButton__Xhqq3")
# page.locator("button.Aside_searchButton__Xhqq3").click()
time.sleep(2)

page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
time.sleep(2)

page.keyboard.down("Enter")
time.sleep(3)

page.click("a#search_tab_position")
time.sleep(3)

for x in range(5):
  page.keyboard.down("End")
  time.sleep(1)

time.sleep(2)

content = page.content()

p.stop()

soup = BeautifulSoup(content, "html.parser")