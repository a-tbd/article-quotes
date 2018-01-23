import spacy
import os

nlp = spacy.load('en')

def main():
    for item in os.listdir('articles_parsed/'):
        if item !='.DS_Store':
            file = open('articles_parsed/' + item, 'r')
            doc = nlp(file.read())

            file.close()

            for ent in doc.ents:
                if ent.label_ == 'PERSON':
                    print(ent.text, ent.start_char, ent.end_char, ent.label_) 


if __name__ == '__main__':
    main()