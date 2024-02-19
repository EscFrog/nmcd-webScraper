import requests
from bs4 import BeautifulSoup

keywords = (
  "flutter",
  "python",
  "golang",
)
user_agent = "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36"
all_Jobs = []


class Job:
  def __init__(self, title, company, loc_arr, link):
    self.title = title.text.strip()
    self.company = company.text.strip()
    self.location = [loc.text.strip() for loc in loc_arr[:-1]]  # 리스트 컴프리헨션을 사용하여 각 위치 텍스트의 공백을 제거. 리스트 컴프리헨션 기억할 것.
    self.salary = loc_arr[-1].text.strip()
    self.link = link
  
  def show_details(self):
    location_str = ", ".join(self.location)
    print("---")
    print(f">>> {self.title} at \"{self.company}\" <---- {self.salary}")
    print(location_str)
    print(f"Link: {self.link}")


def scrape_page(url):
  response = requests.get(url, headers={
  "User-Agent": user_agent,
  })

  soup = BeautifulSoup(
    response.content,
    "html.parser",
    )

  job_blocks = soup.find('table', id='jobsboard').find_all('tr', attrs={'data-offset': True})

  for job_block in job_blocks:
    info_data = job_block.find('td', class_='company_and_position')
    
    title = info_data.find('h2', itemprop='title')
    company = info_data.find('h3', itemprop='name')
    loc_arr = info_data.find_all('div', class_='location')
    link = info_data.find('a', itemprop='url')["href"]

    new_job = Job(title, company, loc_arr, link)
    all_Jobs.append(new_job)


def find_jobs(keywords):
  for keyword in keywords:
    print(f"Finding jobs for {keyword}...")
    url = f"https://remoteok.com/remote-{keyword}-jobs"
    scrape_page(url)
  print(f"I found {len(all_Jobs)} jobs")
  
  answer = input("Would you like to show details? (y/n) > ")
  if answer == "y":
    for job in all_Jobs:
      job.show_details()


find_jobs(keywords)

