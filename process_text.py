import os
from bs4 import BeautifulSoup


def scrape_articles():
    """
    Parse all the downloaded articles from the articles folder
    Remove the useless tags and then save that clean html to the articles_parsed_with_thml folder.
    """
    for article in os.listdir('articles'):
        with open('articles/' + article, 'r') as f:
            soup = BeautifulSoup(f, 'html.parser')

            # Remove these useless tags
            for script in soup(['script', 'style', 'form', 'meta']):
                script.decompose()

            # for text in soup(['div', 'a']):
            #     if class = 'accessibility-ad-header' 'skip-to-text-link'

            # remove the ad tags
            for ad in soup.find_all('div', class_=['accessibility-ad-header', 'newsletter-signup']):
                ad.decompose()

            # remove the useless anchor tag
            for skip_link in soup.find_all('a', class_='skip-to-text-link'):
                skip_link.decompose()   

            # Remove the list of related articles
            for list_tag in soup.find_all('ul', class_='footer'):
                list_tag.decompose()

            # Parse the real story data and send it to new files
            paras = soup.find_all('div', class_="story-body")

            text = '\n'.join([str(para.prettify()) for para in paras])

            with open('articles_parsed_with_html/{}'.format(article), 'w') as new_file:
                new_file.write(text)


if __name__ == '__main__':
    scrape_articles()