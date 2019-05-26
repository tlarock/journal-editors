# journal-editors
Open NetSci Hackathon 2019 project scraping and analyzing members of editorial boards of scientific journals. 

### Idea
The high level idea is to scrape journals for their editorial boards and then create bipartite networks of journals to editors, then co-editorial projections on both people (connected if they edit the same journal) and journals (connected if they share an editor). A longer term goal is to curate a public dataset of editorial boards that researchers can study.

### Tools
We have written python code using the `scrapy` package to extract data from journal websites. We also use `BeautifulSoup` to parse the resulting html.

### Challenges
Unfortunately, many publishers (such as Elsevier and Springer Nature) explicitly disallow scraping from their journal websites. Due to this, we are unable to gather the editorial board data easily without written permission. Getting this permission was not feasible during a 1.5 day hackathon, but is an option for the future.

Other publishers, such as Cambridge and Oxford, do not disallow scraping, so we were able to gather data from them. The challenge then is cleaning the data: the different journal websites list the editors in different formats and with different information (e.g. affiliations). So far, we have focused on only getting names of editors, but we hope to supplement with further information in the future.
