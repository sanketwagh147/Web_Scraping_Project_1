# Scrape timesjobs website
from bs4 import BeautifulSoup
import requests
import time

# Input single skill which is not relevant to the job search
print("Enter not relevant skills")
ignore_skills = input('>')
print(f'Not showing {ignore_skills} related jobs')

def find_jobs():
    html_text = requests.get(r'https://www.timesjobs.com/candidate/job-search.html?searchType=personalizedSearch&from=submit&txtKeywords=python&txtLocation=Pune').text
    # print(html_text)
    soup = BeautifulSoup(html_text, 'lxml')
    jobs = soup.find_all('li', class_ = "clearfix job-bx wht-shd-bx")
    # print(jobs)


    for index, job in enumerate(jobs):
        posting_date = job.find('span', class_="sim-posted").span.text
        if 'few' in posting_date:
            # print((job.text))
            company = job.find('h3', class_="joblist-comp-name").text.replace(" ", "").strip()
            skills = job.find('span', class_="srp-skills").text.replace(" ", "").strip()
            # print(company)
            # print(posting_date)
            # print(skills)
            link = job.header.h2.a['href']
            if ignore_skills not in skills:
                with open(f'scraped_data/{company[:7]}.txt', 'w') as f:  # saves files name as first 8 characters
                    f.write(f'Company Name: {company} \n')
                    f.write(f'Required Skills: {skills} \n')
                    f.write(f'More Info: {link}')
                    f.write("\n")
                print("File Created successfully")

if __name__ == '__main__':
    while True:
        find_jobs()
        time_in_min = 10
        time.sleep(time_in_min * 60)
        print(f"Sleeping for {time_in_min}")