from playwright.sync_api import sync_playwright
import time
from bs4 import BeautifulSoup
import csv

root_url = "https://www.wanted.co.kr"

playwright = sync_playwright().start()

# browser = p.chromium.launch()
browser = playwright.chromium.launch(headless=False)

page = browser.new_page()

page.goto(f"{root_url}/search?query=flutter&tab=position")
# time.sleep(2)

# page.click("button.Aside_searchButton__Xhqq3")
# # page.locator("button.Aside_searchButton__Xhqq3").click() # 이렇게 할 수도 있음
# time.sleep(2)

# page.get_by_placeholder("검색어를 입력해 주세요.").fill("flutter")
# time.sleep(2)

# page.keyboard.down("Enter")
# time.sleep(3)

# page.click("a#search_tab_position")
# time.sleep(3)

for x in range(5):
  page.keyboard.down("End")
  time.sleep(1)

# time.sleep(1)

content = page.content()

playwright.stop()

soup = BeautifulSoup(content, "html.parser")

jobs = soup.find_all("div", class_="JobCard_container__FqChn")

jobs_db = []

for job in jobs:
  link = f'{root_url}{job.find("a")["href"]}'
  title = job.find("strong", class_="JobCard_title__ddkwM").text
  company_name = job.find("span", class_="JobCard_companyName__vZMqJ").text
  reward = job.find("span", class_="JobCard_reward__sdyHn").text
  job = {
    "title": title,
    "company_name": company_name,
    "reward": reward,
    "link": link,
  }
  jobs_db.append(job)

file = open("jobs.csv", "w")
writer = csv.writer(file)
writer.writerow([ # 일단 헤더 행을 만든다.
  "Title",
  "Company",
  "Reward",
  "Link"
])

for job in jobs_db:
  writer.writerow(job.values()) # dictionary.values 메소드는 딕셔너리의 값만 리스트로 만들어 반환한다.