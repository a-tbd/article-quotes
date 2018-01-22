import os
from bs4 import BeautifulSoup


def scrape_article():
    for article in os.listdir('articles'):
        with open('articles/' + article, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            for script in soup(['script', 'style']):
                script.decompose()

            for ad in soup.find_all('div', class_='accessibility-ad-header'):
                ad.decompose()

            for skip_link in soup.find_all('a', class_='skip-to-text-link'):
                skip_link.decompose()

            paras = soup.find_all('div', class_="story-body")

            text = '\n'.join([str(para) for para in paras])

            with open('articles_parsed_with_html/{}'.format(article), 'w') as new_file:
                new_file.write(text)

if __name__ == '__main__':
    scrape_article()