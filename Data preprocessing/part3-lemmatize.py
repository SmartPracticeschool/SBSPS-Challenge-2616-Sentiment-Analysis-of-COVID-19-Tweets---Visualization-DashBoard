import nltk
from nltk.stem import WordNetLemmatizer
from nltk.corpus import wordnet

lemmatizer = WordNetLemmatizer()

''' This function assigns the wordnet tag of pos tag'''
''' The nltk pos tags for adjective is JJ and for verb is VRB and for Noun is NN and for adverb is RB''' 
def nltk_tag_to_wordnet(nltk_tag):
    if nltk_tag.startswith('J'):
        return wordnet.ADJ
    elif nltk_tag.startswith('V'):
        return wordnet.VERB
    elif nltk_tag.startswith('N'):
        return wordnet.NOUN
    elif nltk_tag.startswith('R'):
        return wordnet.ADV
    else:          
        return None

def lemmatize_my_sentence(sentence):
    #tokenize the sentence and find the POS tag for each token
    nltk_tagged_assign = nltk.pos_tag(nltk.word_tokenize(sentence))  
    
    wordnet_tag = map(lambda x: (x[0], nltk_tag_to_wordnet(x[1])), nltk_tagged_assign)
    lemmatized_sentence = []
    for word, tag in wordnet_tag:
        if tag is None:
            #if there is no available tag, append the token as is
            lemmatized_sentence.append(word)
        else:        
            #else use the tag to lemmatize the token
            lemmatized_sentence.append(lemmatizer.lemmatize(word, tag))
    return " ".join(lemmatized_sentence)
