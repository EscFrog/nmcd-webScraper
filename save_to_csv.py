import csv

def save_to_csv(keyword, jobs_list): 
  filename = f"{keyword}_jobs.csv" 
  with open(filename, "w", newline='', encoding='utf-8') as file:
    writer = csv.writer(file)
    writer.writerow(["Title", "Company", "Reward", "Link"])

    for job in jobs_list:
      writer.writerow(job.get_property_list())
    
  return filename