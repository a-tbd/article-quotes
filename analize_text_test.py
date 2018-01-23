import spacy

import pprint

pp = pprint.PrettyPrinter(indent=4)

nlp = spacy.load('en')

def main():

    file = open('articles_parsed/a-sense-of-dread-for-civil-servants-shaken-by-trump-transition.html.txt', 'r')
    doc = nlp(file.read())

    file.close()

    data = {
        'names': set(),
        'n_names': 0,
        'article_name': 'a-sense-of-dread-for-civil-servants-shaken-by-trump-transition.html.txt',
        'sentences':{}
    }

    # Let's look at the sentences
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
    
    # for ent in doc.ents:
    #     if ent.label_ == 'PERSON':
    #         # print(ent.text, ent.start_char, ent.end_char, ent.label_) 
    #         data['names'].add(ent.text)

    data['n_names'] = len(data['names'])


    # We save names per sentence, it will repeat full names and last names as two different person, so if Donald J. Trup appears, it will say two person entities appear, Donald J. Trump and Trump
    for key, sent in enumerate(sents):
        data['sentences'][key] = []
        for person in all_names.keys():
            if person in sent:
                data['sentences'][key].append(person)
    # for key, sent in enumerate(sents):
    #     data['sentences'][key] = []
    #     for person in data['names']:
    #         if person in sent:
                
    #             # print(data['sentences'])
    #             data['sentences'][key].append(person)
                
    

    

    pp.pprint(len(all_names))
    pp.pprint(all_names)
    pp.pprint(data)

    


if __name__ == '__main__':
    main()