#!python3.10
import cloudscraper
from bs4 import BeautifulSoup
import os

import argparse


file_name = 'jobs_posted.html'

if os.path.exists(file_name):
    os.remove(file_name)


def extract_jobs_from_indeed(job="data+scientist+intern", num_of_pages=1):
    scraper = cloudscraper.create_scraper() 

    search_urls = [
        f"https://www.indeed.com/jobs?q={job}&l=&vjk=d99fe42f8e6e2bc5"
    ]

    for idx in range(2, num_of_pages+1):
        search_urls.append(
            f"https://www.indeed.com/jobs?q={job}&l=&&start={idx}0&vjk=d99fe42f8e6e2bc5"
        )

    pages = [
        scraper.get(r_url) for r_url in search_urls
    ]

    soups = [
        BeautifulSoup(page.content, "html.parser") for page in pages
    ]

    filter_words = ["fccid"]
    print(soups)
    for soup in soups:
        extract_job_list(soup, filter_words)

def extract_job_list(soup, filter_words):
    job_list = str(soup.find(id="mosaic-provider-jobcards"))
    anchor_links = BeautifulSoup(job_list, "html.parser").find_all('a')
    job_links = [
        link for link in anchor_links
        if all(filter in str(link) for filter in filter_words)
    ]

    for job_link in job_links:
        job_link['href'] = "https://www.indeed.com" + str(job_link["href"])

    #Adding brs between links
    final_job_tags = [
        str(link) for link in job_links
    ]

    final_display_tag_string = (" <br> ").join(final_job_tags)


    if os.path.exists(file_name):
        append_write = 'a' # append if already exists
    else:
        append_write = 'w' # make a new file if not

    with open(file_name, append_write) as f:
        f.write(final_display_tag_string)


if __name__ == '__main__':
    parser=argparse.ArgumentParser()

    parser.add_argument("--pages", help="pages to parse")
    parser.add_argument("--job", help="Job title, default(data science intern)")
    args=parser.parse_args()
    pages = args.pages or 1
    job_title = args.job or "data+scientist+intern"
    job_title = job_title.replace(" ", "+")

    extract_jobs_from_indeed(job_title, int(pages))

#python new_intern_cloud_scraper.py --pages 3 --job "data scientist intern"