import requests
import sys
from bs4 import BeautifulSoup
import re
import csv

max_crawl = 5
headers = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64)"
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrom/113.0.0.0 Safari/537.36"
}
def crawler(target):
    urls = [target]
    crawl = 0

    while urls and crawl < max_crawl:
        current = urls.pop(0)
        response = requests.get(target, headers=headers)
        soup = BeautifulSoup(response.text, "html.parser")
        print("[DEBUG] Request Headers:", response.request.headers)
        elements = soup.select("a[href]")
        for link_element in elements:
            url = link_element["href"]

            if not url.startswith("http"):
                absolute_url = requests.compat.urljoin(current, url)
            else:
                absolute_url = url

            if (
                absolute_url.startswith(target)
            and absolute_url not in urls
            ):
                urls.append(absolute_url)
        print(urls)
        crawl += 1
if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: Python3 WebCsrawler.py <url>")
        sys.exit()
    else:
        crawler(sys.argv[1])
