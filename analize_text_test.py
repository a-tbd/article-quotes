import spacy
import csv
import pprint
import pdb
import difflib

pp = pprint.PrettyPrinter(indent=4)

nlp = spacy.load('en')

def parse_article(file_name):

    file = open(file_name, 'r')
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
        # pdb.set_trace()
        if len(span) > 1:
            sents.append(span.text.strip())
        else:
            print(span.start, span.text)
    
       
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
        data['sentences'][key] = {'people':[],'text':sent}
        for person in all_names.keys():
            if person in sent:
                data['sentences'][key]['people'].append(person)

    return data
    

def write_to_csv(data):
    '''Write data from parsed articles to csv file in the following format:
    title | sentence number | sentence text | persons in article | names of people quoted
    '''
    open('sentences.csv', 'w').close()
    for key in data['sentences']:
        with open('sentences.csv', 'a') as output_file:
            writer = csv.writer(output_file)
            new_entry = [data['article_name'], key, data['sentences'][key]['people'], data['sentences'][key]['text']]
            writer.writerow(new_entry)
    # pp.pprint(data)


def test():
    data = parse_article('a-sense-of-dread-for-civil-servants-shaken-by-trump-transition.html.txt')

    file = open('a-sense-of-dread-for-civil-servants-shaken-by-trump-transition.html.txt', 'r')
    text = file.read()
    file.close()

    recreate_text = ''.join([data['sentences'][entry]['text'] for entry in data['sentences']])
    
    for i,s in enumerate(difflib.ndiff(recreate_text, text)):
        if s[0] == ' ': 
            continue
        elif s[0] == '-':
            print('Delete "{}" from {}'.format(s[-1], i))
        elif s[0] == '+':
            print('Add "{}" from {}'.format(s[-1], i))

    # assert recreate_text == text

    print('test complete')




def main(file_name):
    data = parse_article(file_name)
    write_to_csv(data)

if __name__ == '__main__':
    # main('articles_parsed/a-sense-of-dread-for-civil-servants-shaken-by-trump-transition.html.txt')
    test()
    