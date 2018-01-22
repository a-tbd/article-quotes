import spacy
import os
import itertools
import io

nlp = spacy.load('en')

def get_sentences():
    for item in os.listdir('articles_parsed/'):
        with io.open('articles_parsed/' + item, 'r', encoding='utf-8') as f:
            doc = nlp(f)
            count = 0

            for sentence in doc.sents:
                with open('sentences.csv', 'a') as output_file:
                    count += 1
                    new_entry = u'{}, {}, {}\n'.format(item, count, sentence.text)
                    output_file.write(new_entry)


if __name__ == '__main__':
    get_sentences()
    open('sentences.csv', 'w').close()