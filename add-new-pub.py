import os
import json

publication = json.load(open('publication.json','r'))

user = os.environ['GITHUB_ACTOR']
print(user)

pub_title = publication['pub_title']
year_of_pub = publication['year_of_pub']
tldr = publication['tldr']
pub_link = publication['pub_link']

content = f"\n| {pub_title} | {year_of_pub} | {tldr} | {pub_link} | [@{user}](https://github.com/{user}) |"
pubs_file_path = os.path.join(os.getcwd(), './refs-catalog/docs/pubs.md');

with open(pubs_file_path, "a") as file_pub:
  file_pub.write(content)

os.remove('./publication.json')
