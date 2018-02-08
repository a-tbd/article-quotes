import spacy
import os

nlp = spacy.load('en')

def main():
    article_fnames = [fname for fname in os.listdir('articles_parsed/') if fname != '.DS_Store']
    for item in article_fnames:
        file = open('articles_parsed/' + item, 'r')
        doc = nlp(file.read())

        file.close()

        # meta information for article
        data = {
            'names': set(),
            'n_names': 0,
            'article_name': 'a-sense-of-dread-for-civil-servants-shaken-by-trump-transition.html.txt',
            'sentences':{}
        }

        sents = []
        # the "sents" property returns spans
        # spans have indices into the original string
        # where each index value represents a token
        for span in doc.sents:
            # go from the start to the end of each span, returning each token in the sentence
            # combine each token using join()
            sent = ''.join(doc[i].string for i in range(span.start, span.end)).strip()
            sents.append(sent)

        all_names = {}
        for ent in doc.ents:
            if ent.label_ == 'PERSON':
                name_parts = ent.text.split(' ')
                if len(name_parts) > 1:
                    last_name = name_parts[-1]
                    if not last_name in all_names:
                        all_names[last_name] = [ent.text]
                    else:
                        all_names[last_name].append(ent.text)

        data['n_names'] = len(data['names'])

        for key, sent in enumerate(sents):
            data['sentences'][key] = []
            for person in all_names.keys():
                if person in sent:
                    data['sentences'][key].append(person)


if __name__ == '__main__':
    main()
