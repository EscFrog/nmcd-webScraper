from flask import Flask, render_template
from extractors.wanted import scrape_wanted
from save_to_csv import save_to_csv

app = Flask("JobScrapper")

@app.route("/")
def home():
  return render_template("home.html")

@app.route("/search")
def search():
  return render_template("search.html", keyword)

app.run("127.0.0.1", debug=True)

# keyword = "python"

# jobs_list = scrape_wanted(keyword)

# for job in jobs_list:
#     print(job.get_info())

# save_to_csv(keyword, jobs_list)