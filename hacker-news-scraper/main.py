import requests
from bs4 import BeautifulSoup
import pprint

res = requests.get('https://news.ycombinator.com/news', timeout=60)
res2 = requests.get('https://news.ycombinator.com/news?p=2', timeout=60)

soup = BeautifulSoup(res.text, 'html.parser')
soup2 = BeautifulSoup(res2.text, 'html.parser')

scraped_links = soup.select('.titleline')
scraped_subtext = soup.select('.subtext')

scraped_links2 = soup2.select('.titleline')
scraped_subtext2 = soup2.select('.subtext')

mega_links = scraped_links + scraped_links2
mega_subtext = scraped_subtext2 + scraped_subtext2

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse = True)

def create_custom_hn(links, subtext):
    hn = []

    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 99:
                hn.append({
                    'title': title,
                    'link': href,
                    'votes': points
                  })

    return sort_stories_by_votes(hn)

pprint.pprint(create_custom_hn(mega_links, mega_subtext))
