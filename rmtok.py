import requests
from bs4 import BeautifulSoup

keywords = (
  "flutter",
  "python",
  "golang",
)

dataToSend = {
  "url": "https://remoteok.com/remote-flutter-jobs",
  "user_agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36",
}

all_Jobs = []

class Job:
  def __init__(self, title, company, loc_arr, link):
    self.title = title.text
    self.company = company.text
    self.location = []
    for i in range(len(loc_arr) - 1):
      self.location.append(loc_arr[i].text)
    self.salary = loc_arr[-1].text
    self.link = link
  
  def show_details(self):
    print(f"""
    *************************
    {self.title}
    {self.company}
    {self.location}
    {self.salary}
    {self.link}
    """)

def scrape_page():
  response = requests.get(dataToSend["url"], headers={
  "User-Agent": dataToSend["user_agent"],
  })

  soup = BeautifulSoup(
    response.content,
    "html.parser",
    )

  jobs = soup.find('table', id='jobsboard').find_all('tr', attrs={'data-offset': True})

  for job in jobs:
    info_data = job.find('td', class_='company_and_position')
    
    title = info_data.find('h2', itemprop='title')
    company = info_data.find('h3', itemprop='name')
    loc_arr = info_data.find_all('div', class_='location')
    link = info_data.find('a', itemprop='url')["href"]

    new_job = Job(title, company, loc_arr, link)
    all_Jobs.append(new_job)

scrape_page()

for job in all_Jobs:
  job.show_details()