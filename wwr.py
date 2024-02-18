import requests
from bs4 import BeautifulSoup

all_jobs = []

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
    job_data = {
        "title": title,
        "company": company.text,
        "position": position.text,
        "region": region.text,
        "link": f"https://weworkremotely.com{link}",
    }
    all_jobs.append(job_data)


def get_pages(url):
  response = requests.get(url)
  soup = BeautifulSoup(response.content, "html.parser")
  return len(soup.find("div", class_="pagination").find_all("span", class_="page"))

total_pages = get_pages("https://weworkremotely.com/remote-full-time-jobs")

for x in range(total_pages):
  url = f"https://weworkremotely.com/remote-full-time-jobs?page={x+1}"
  scrape_page(url)

print(len(all_jobs))