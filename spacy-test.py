import spacy
from spacy.symbols import nsubj, npadvmod, VERB
from spacy.language import EntityRecognizer
from genderPredictor import genderPredictor

nlp = spacy.load('en')
predict = genderPredictor()
predict.trainAndTest()

def get_quotes():
	words_to_match = set(['said', 'asked', 'added', 'noted', 'replied', 'responded', 'wrote', 'emailed', 'stated', 'accused', 'shouted', 'demanded'])

	f = open('articles.txt', 'rU').read()
	dtxt = f.decode('utf-8')
	doc = nlp(dtxt)

	n_chunks = [n for n in doc.noun_chunks]
	all_people = {n.root: n for n in n_chunks if n.root.ent_type_ == 'PERSON'} # some ppl are missing from the lookup table

	speakers_sing = []
	genders = {'F': 0, 'M': 0, 'O': 0, 'Error': 0}
	for possible_verb in doc:
		if possible_verb.lower_ in words_to_match:

			possible_subs = [c for c in possible_verb.subtree if c.dep == nsubj or c.dep == npadvmod]

			for c in possible_subs:
				speaker = None
				if c.tag_ == 'NNP':
					try:
						speaker = all_people[c] # this is only looking up noun chunks
					except:
						start = next((child.i for child in c.lefts if child.ent_type_ == 'PERSON'), c.i) # http://www.goodmami.org/2013/01/30/Getting-only-the-first-match-in-a-list-comprehension.html
						end = next((child.i for child in c.rights if child.ent_type_ == 'PERSON'), c.i) #TODO does this work for Mr.?
						speaker = doc[start:end+1]
						all_people[c] = speaker
				elif c.tag_ == 'PRP':
					speaker = c
					
				if speaker:
					gender = get_gender(speaker)
					genders[gender] += 1 # I THEY IT YOU
					speakers_sing.append((speaker, gender, doc[possible_verb.left_edge.i:possible_verb.right_edge.i+1]))

	return genders

def get_gender(name):
	if name.lower_ == 'he':
		return 'M'
	elif name.lower_ == 'she':
		return 'F'
	else:
		try: 
			first_name = next((n for n in name), name)
			if first_name.lower_ == 'mr.':
				return 'M'
			elif first_name.lower_ == 'ms.' or first_name.lower_ == 'miss' or first_name.lower_ == 'ms.':
				return 'F'
			else:
				return predict.classify(first_name.text)
		except:
			return 'Error'

print get_quotes()

