import spacy

nlp = spacy.load('en')

def main():

    file = open('articles_parsed/-dana-boente-attorney-general-acting.html.txt', 'r')
    doc = nlp(file.read())

    file.close()

    for ent in doc.ents:
        if ent.label_ == 'PERSON':
            print(ent.text, ent.start_char, ent.end_char, ent.label_) 


if __name__ == '__main__':
    main()