const fs = require('fs');
const path = require('path');
const eventPayload = require(process.env.GITHUB_EVENT_PATH);
const publication = require('./publication.json');

const user = eventPayload.sender.login;
const [pub_title, year_of_pub, tldr, pub_link] = Object.values(publication);
const content = `\n| ${pub_title} | ${year_of_pub} | ${tldr} | ${pub_link} | [@${user}](https://github.com/${user}) |`;
const pubsFilePath = path.join(__dirname, '/refs-catalog/docs/pubs.md');

fs.appendFileSync(pubsFilePath, content);
