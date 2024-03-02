from playwright.sync_api import sync_playwright
from bs4 import BeautifulSoup
import time
import csv

root_url="https://www.wanted.co.kr"
prog_langs = [
  "flutter",
  "next.js",
  "kotlin"
  ]

class Job:
  def __init__(self, title, company, reward, link):
    self.title = title
    self.company = company
    self.reward = reward
    self.link = link

  def get_info(self):
    return [self.title, self.company, self.reward, self.link]


def auto_scroll(page):
  last_height = page.evaluate("document.body.scrollHeight")

  while True:
    page.evaluate("window.scrollTo(0, document.body.scrollHeight)")
    time.sleep(1)

    new_height = page.evaluate("document.body.scrollHeight")
    if new_height == last_height:
      break
    last_height = new_height


def save_to_csv(prog_lang, Jobs_list): 
  with open(f"{prog_lang}_jobs.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Reward", "Link"])

    for job in Jobs_list:
      writer.writerow(job.get_info())


def scrape_infinite_scroll_page(prog_lang):
  url = f"{root_url}/search?query={prog_lang}&tab=position"
  Jobs_list = []

  with sync_playwright() as p:
    browser = p.chromium.launch(headless=False)
    page = browser.new_page()
    page.goto(url)

    auto_scroll(page)
    
    content = page.content()

  soup = BeautifulSoup(content, "html.parser")
  jobs = soup.find_all("div", class_="JobCard_container__FqChn")

  for job in jobs:
    title = job.find("strong", class_="JobCard_title__ddkwM").text
    company = job.find("span", class_="JobCard_companyName__vZMqJ").text
    reward = job.find("span", class_="JobCard_reward__sdyHn").text
    link = f'{root_url}{job.find("a")["href"]}'
    
    job_instance = Job(title, company, reward, link)
    Jobs_list.append(job_instance)
  
  save_to_csv(prog_lang, Jobs_list)

for prog_lang in prog_langs:
  scrape_infinite_scroll_page(prog_lang)