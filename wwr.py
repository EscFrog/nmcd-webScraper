import requests
from bs4 import BeautifulSoup

all_jobs = []

class Job_data():
  def __init__(self, title, company, position, region, link):
    self.title = title
    self.company = company.text
    self.position = position.text
    self.region = region.text
    self.link = f"https://weworkremotely.com{link}"
  
  def show_detail(self):
    print(f"""
    {self.title}
    {self.company}
    {self.position}
    {self.region}
    """)

def scrape_page(url):
  print(f"Scraping {url}...")
  response = requests.get(url)
  
  soup = BeautifulSoup(
      response.content,
      "html.parser",
  )

  jobs = soup.find("section", class_="jobs").find_all("li")[1:-1]

  for job in jobs:
    title = job.find("span", class_="title").text
    link = job.find("div", class_="tooltip--flag-logo").next_sibling[
        "href"]  #[] 안은 attribute를 말한다. 딕셔너리 형태로 attribute를 가져오기 때문.
    company, position, region = job.find_all("span", class_="company")
    all_jobs.append(Job_data(title, company, position, region, link))


def get_pages(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  return len(soup.find("div", class_="pagination").find_all("span", class_="page"))


def start():
  total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs")

  for x in range(total_pages):
    url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
    scrape_page(url)

  print(f"*** You found {len(all_jobs)} jobs ***")
  go_sign = input("Would you like to see the list of details? (y/n) >")
  if go_sign == "y":
    for job in all_jobs:
      job.show_detail()

start()
