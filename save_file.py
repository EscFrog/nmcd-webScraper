import csv

def save_to_csv(keyword, Jobs_list): 
  with open(f"{keyword}_jobs.csv", "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Reward", "Link"])

    for job in Jobs_list:
      writer.writerow(job.get_info())