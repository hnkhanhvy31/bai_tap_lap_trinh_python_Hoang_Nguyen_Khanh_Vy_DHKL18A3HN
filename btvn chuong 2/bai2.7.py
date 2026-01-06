import requests
import xml.etree.ElementTree as ET
import csv

url = "https://vnexpress.net/rss/tin-moi-nhat.rss"
response = requests.get(url)
root = ET.fromstring(response.content)

items = root.findall(".//item")

with open("rss_news.csv", "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["title", "link", "pubDate", "description"])

    for item in items:
        title = item.findtext("title")
        link = item.findtext("link")
        pubDate = item.findtext("pubDate")
        desc = item.findtext("description")
        writer.writerow([title, link, pubDate, desc])

print("Đã lưu RSS vào file rss_news.csv")
