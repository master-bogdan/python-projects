import unittest
from unittest.mock import patch, MagicMock
from bs4 import BeautifulSoup
from scraper import create_custom_hn, get_info

class TestHackerNewsScraper(unittest.TestCase):

    @patch('scraper.requests.get')
    def test_get_info(self, mock_get):
        # Mock the get request and its response
        mock_html = '<html><body><div class="titleline">Title 1</div><div class="subtext">Subtext 1</div></body></html>'
        mock_response = MagicMock()
        mock_response.text = mock_html
        mock_get.return_value = mock_response

        # Call get_info and check results
        links, subtext = get_info('http://fakeurl.com')
        self.assertEqual(len(links), 1)
        self.assertEqual(len(subtext), 1)

    @patch('scraper.get_info')
    def test_create_custom_hn(self, mock_get_info):
        # Mocking the get_info function
        link_element = BeautifulSoup('<a href="http://fakeurl.com/story">Story 1</a>', 'html.parser')
        score_element = BeautifulSoup('<span class="score">150 points</span>', 'html.parser')
        mock_get_info.return_value = ([link_element], [score_element])

        # Call create_custom_hn and check results
        result = create_custom_hn('http://fakeurl.com')
        self.assertEqual(len(result), 1)
        self.assertIn('Story 1', result[0]['title'])
        self.assertEqual(result[0]['votes'], 150)

if __name__ == '__main__':
    unittest.main()
