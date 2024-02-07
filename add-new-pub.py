import os
import json

ev_payload = os.environ['GITHUB_EVENT_PATH']
publication = json.load(open('publication.json','r'))
print(publication)
print(ev_payload)

user = ev_payload['sender']['login']
pub_title = publication['title']
year_of_pub = publication['year_of_pub']
tldr = publication['tldr']
pub_link = publication['pub_link']

content = f"\n| {pub_title} | {year_of_pub} | {tldr} | {pub_link} | [@{user}](https://github.com/{user}) |"
pubs_file_path = os.path.join(os.getcwd(), '/refs-catalog/docs/pubs.md');

with open(pubs_file_path, "a") as file_pub:
  file_pub.write(content)

os.remove('./publication.json')
