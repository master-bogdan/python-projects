import requests
from bs4 import BeautifulSoup

def get_info(*url):
    scraped_links = []
    scraped_subtext = []

    for page in url:
        res = requests.get(page, timeout=60)
        soup = BeautifulSoup(res.text, 'html.parser')
        scraped_links += soup.select('.titleline')
        scraped_subtext += soup.select('.subtext')

    return [scraped_links, scraped_subtext]

def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key = lambda k:k['votes'], reverse = True)

def create_custom_hn(*page_urls):
    hn = []
    links, subtext = get_info(*page_urls)

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