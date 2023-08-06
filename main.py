import spacy

# Load the SpaCy English model
nlp = spacy.load("en_core_web_sm")

# Sample text to process
text = "SpaCy is an awesome library for natural language processing!"

# Process the text
doc = nlp(text)

# Print the tokenized words and their part-of-speech tags
for token in doc:
    print(token.text, token.pos_)

# Print the named entities
for entity in doc.ents:
    print(entity.text, entity.label_)