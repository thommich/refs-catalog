const fs = require('fs');
const path = require('path');
const eventPayload = require(process.env.GITHUB_EVENT_PATH);
const publication = require('./publication.json');

const user = eventPayload.sender.login;
const [pub_title, year_of_pub, tldr, pub_link] = Object.values(publication);
console.log(pub_title)

const content = `| ${pub_title} | ${year_of_pub} | ${tldr} | ${pub_link} | [@${user}](https://github.com/${user}) |`;
console.log(content)

const pubsFilePath = path.join(__dirname, '/refs-catalog/pubs.md');
console.log(pubsFilePath)
fs.appendFileSync(pubsFilePath, content);
