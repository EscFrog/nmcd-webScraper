from flask import Flask
from extractors.wanted import scrape_wanted
from save_to_csv import save_to_csv

app = Flask("JobScrapper")

@app.route("/")
def home():
  return 'Hello World!'

app.run("127.0.0.1", debug=True)

# keyword = "python"

# jobs_list = scrape_wanted(keyword)

# for job in jobs_list:
#     print(job.get_info())

# save_to_csv(keyword, jobs_list)