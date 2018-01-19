import os
from bs4 import BeautifulSoup


def scrape_article():
    for article in os.listdir('articles'):
        with open('articles/' + article, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            paras = soup.find_all('p', 'story-body-text')

            text = '\n'.join([para.get_text() for para in paras])

            with open('articles_parsed/{}.txt'.format(article), 'w') as new_file:
                new_file.write(text)

scrape_article()