import os
from bs4 import BeautifulSoup


def scrape_article():
    for article in os.listdir('articles'):
        with open('articles/' + article, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')
            paras = soup.find_all('p', 'story-body-text', text=True)
            # text = [p.string.encode('utf-8') if p.string is not None else '' for p in paras]
            # tex t = paras.get_text()

            text = '\n'.join([para.get_text() for para in paras])
            print(text)



            with open('articles_parsed/{}.txt'.format(article), 'a') as new_file:
                new_file.write(text)


        # text = os.path.splitext(article)
        # soup = BeautifulSoup(text, 'html.parser')

        # paras = soup.find_all('p', 'story-body-text')
        # text = [p.string.encode('utf-8') if p.string is not None else '' for p in paras]

        
        # with open('articles_parsed/articles.txt', 'a') as f:
        #     f.write('\n'.join(text))

scrape_article()