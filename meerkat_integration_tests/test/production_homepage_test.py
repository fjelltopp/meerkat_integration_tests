from unittest import TestCase

import requests
from bs4 import BeautifulSoup


countries = {
    "jordan": {
        'url': "https://jordan.emro.info",
        'title': "jordan"
    },
    "rms": {
        'url': "https://rms.emro.info",
        'title': "rms"
    },
    "madagascar": {
        'url': "https://madagascar.emro.info",
        'title': "madagascar"
    },
    "puntland": {
        'url': "https://puntland.emro.info",
        'title': "puntland"
    },
    "somaliland": {
        'url': "https://somaliland.emro.info",
        'title': "somaliland"
    },
    "southcentral": {
        'url': "https://southcentral.emro.info",
        'title': "somalia"
    }
}

class TestHomePage(TestCase):
    def setUp(self):
        pass

    def test_smoke_homepage_and_title(self):
        for country in countries.values():
            url = country['url']
            expected_title = country['title']
            res = requests.get(url)
            self.assertEqual(200, res.status_code)
            html = BeautifulSoup(res.text, "html.parser")
            self.assertIn(expected_title, repr(html.title).lower())

