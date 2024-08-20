from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
import csv
import time

def fetch_jobs(driver, job_titles):
    job_list = []
    elements = driver.find_elements(By.CLASS_NAME, 'job_listing')  
    for element in elements:
        title = element.find_element(By.TAG_NAME, 'h2').text  
        if any(job_title in title for job_title in job_titles):
            job_list.append(title)
        time.sleep(1)  
    return job_list

def save_to_csv(job_list, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Job Title'])
        for job in job_list:
            writer.writerow([job])
    print(f"Data saved to {filename}")

job_titles = [
    "Software Engineer Intern", 
    "Software Developer Intern",
    "Software Engineer New Graduates", 
    "Software Engineer New Grads",
    "Software Engineer New Grad", 
    "Software Engineer Winter Graduates",
    "Software Engineer Winter Grads", 
    "Software Engineer December Grads",
    "Software Engineer January Grads",
    "Mega-Brain Guy"
]

options = Options()
options.headless = True  
driver = webdriver.Chrome(options=options)

url = " "
driver.get(url)
time.sleep(2)  

jobs = fetch_jobs(driver, job_titles)
if jobs:
    save_to_csv(jobs, 'recent_job_postings.csv')

driver.quit()
