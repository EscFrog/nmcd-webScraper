from flask import Flask, render_template, request, redirect, send_file
from extractors.wanted import scrape_wanted_jobs
from save_to_csv import save_to_csv

app = Flask("JobScrapper")
db = {}


@app.route("/")
def home():
  return render_template("home.html")


@app.route("/search")
def search():
  req_keyword = request.args.get("keyword")

  if req_keyword == None:
    return redirect("/")
  
  if req_keyword in db:
    wanted_jobs = db[req_keyword]
  else:
    wanted_jobs = scrape_wanted_jobs(req_keyword)
    db[req_keyword] = wanted_jobs
  
  return render_template("search.html", keyword=req_keyword, jobs = wanted_jobs)


@app.route("/export")
def export():
  req_keyword = request.args.get("keyword")

  if req_keyword == None:
    return redirect("/")
  
  if req_keyword not in db:
    return redirect(f"/search?keyword={req_keyword}")
  
  filename = save_to_csv(req_keyword, db[req_keyword])

  return send_file(filename, as_attachment=True)


app.run("127.0.0.1", debug=True)