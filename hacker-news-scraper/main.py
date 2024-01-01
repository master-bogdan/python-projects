from scraper import create_custom_hn
import pprint

PAGE1_URL = 'https://news.ycombinator.com/news'
PAGE2_URL = 'https://news.ycombinator.com/news?p=2'

pprint.pprint(create_custom_hn(PAGE1_URL, PAGE2_URL))
