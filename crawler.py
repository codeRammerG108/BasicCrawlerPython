import requests
from bs4 import BeautifulSoup


url = "http://stevescooking.blogspot.com/"


response = requests.get(url)


soup = BeautifulSoup(response.text, "html.parser")


links = soup.find_all("a")


with open("links.txt", "w") as file:
    for link in links:
        href = link.get("href")
        if href:
            file.write(href + "\n")

print("Crawling and link extraction complete. Links are saved in links.txt")
