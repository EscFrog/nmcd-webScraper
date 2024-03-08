from extractors.wanted import scrape_wanted
from save_to_csv import save_to_csv

keyword = "python"

jobs_list = scrape_wanted(keyword)

for job in jobs_list:
    print(job.get_info())

save_to_csv(keyword, jobs_list)