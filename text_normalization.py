import string
import nltk
from nltk.corpus import stopwords
from nltk.stem.porter import PorterStemmer
from nltk.stem import WordNetLemmatizer



def load_data():
    filename = './data/data.txt' #change the filepath as per your reference.
    file = open(filename, 'r+')
    text = file.read()
    file.close()
    words = nltk.word_tokenize(text)
    wordslower = nltk.word_tokenize(case_folding(text))
    print("******************************************************************With Punctuation stats******************************************************************")
    token_with_punctuation(words)
    print("******************************************************************Case Folding with Punctuation stats******************************************************************")
    token_with_punctuation(wordslower)
    print("******************************************************************Without Punctuation stats******************************************************************")
    token_without_punctuation(words)
    print("******************************************************************Case Folding without Punctuation stats******************************************************************")
    token_without_punctuation(wordslower)

def stopwords_removal(words):
    stop_text = [];
    stop_words = set(stopwords.words('english'))
    for r in words:
        if not r in stop_words:
            stop_text.append(r)
    my_dict_stopword = {i: stop_text.count(i) for i in stop_text}
    c = list(zip(my_dict_stopword.values(), my_dict_stopword.keys()))
    return c, stop_text


def stemming_words(words):
    stem_words = []
    porter_stemmer = PorterStemmer()
    for i in words:
        stem_words.append(porter_stemmer.stem(i))
    my_dict_tokens_stem = {i: stem_words.count(i) for i in stem_words}
    stem_dist_tokens = list(zip(my_dict_tokens_stem.values(), my_dict_tokens_stem.keys()))
    return stem_words, stem_dist_tokens


def lemmatizing_words(words):
    lemma_words = []
    wordnet_lemmatizer = WordNetLemmatizer()
    for i in words:
        lemma_words.append(wordnet_lemmatizer.lemmatize(i, pos="v"))
    my_dict_tokens_lemma = {i: lemma_words.count(i) for i in lemma_words}
    lemma_dist_tokens = list(zip(my_dict_tokens_lemma.values(), my_dict_tokens_lemma.keys()))
    return lemma_words, lemma_dist_tokens

def case_folding(text):
    return text.lower()

def token_with_punctuation(words):
    stats = []
    stats2 = []
    stats3 = []
    stats4 = []
    stats5 = []
    stats6 = []
    my_dict_tokens = {i: words.count(i) for i in words}
    a = list(zip(my_dict_tokens.values(), my_dict_tokens.keys()))
    a.sort(reverse = True)
    for i in range(1,11):
        stats.append(a[i])
    print("Number of Tokens with punctuation {}".format(len(words)))
    print("Number of type with punctuation {}".format(len(a)))
    print("Top 10 Tokens with punctuation: {}".format(stats))
    print("****************Stemming****************")
    stem_words, stem_dist_tokens = stemming_words(words)
    stem_dist_tokens.sort(reverse=True)
    for i in range(1, 11):
        stats3.append(stem_dist_tokens[i])
    print("Number of Tokens with punctuation and stemming {}".format(len(stem_words)))
    print("Number of type with punctuation and stemming {}".format(len(stem_dist_tokens)))
    print("Top 10 Tokens with punctuation and stemming: {}".format(stats3))
    print("****************Lemmatization****************")
    lemma_words, lemma_dist_tokens = lemmatizing_words(words)
    lemma_dist_tokens.sort(reverse=True)
    for i in range(1, 11):
        stats5.append(lemma_dist_tokens[i])
    print("Number of Tokens with punctuation and Lemmatization {}".format(len(lemma_words)))
    print("Number of type with punctuation and Lemmatization {}".format(len(lemma_dist_tokens)))
    print("Top 10 Tokens with punctuation and Lemmatization: {}".format(stats5))

    c, stop_text = stopwords_removal(words)
    c.sort(reverse=True)
    for i in range(1,11):
        stats2.append(c[i])
    print("****************Stop words Removed****************")
    print("Number of Tokens with punctuation and removing stop words {}".format(len(stop_text)))
    print("Number of type with punctuation and removing stop words {}".format(len(c)))
    print("Top 10 Tokens with punctuation and removing stop words: {}".format(stats2))
    print("****************Stemming****************")
    stem_words, stem_dist_tokens = stemming_words(stop_text)
    stem_dist_tokens.sort(reverse=True)
    for i in range(1, 11):
        stats4.append(stem_dist_tokens[i])
    print("Number of Tokens with punctuation and removing stop words and stemming {}".format(len(stem_words)))
    print("Number of type with punctuation and removing stop words and stemming {}".format(len(stem_dist_tokens)))
    print("Top 10 Tokens with punctuation and removing stop words and stemming: {}".format(stats4))
    print("****************Lemmatization****************")
    lemma_words, lemma_dist_tokens = lemmatizing_words(stop_text)
    lemma_dist_tokens.sort(reverse=True)
    for i in range(1, 11):
        stats6.append(lemma_dist_tokens[i])
    print("Number of Tokens with punctuation and removing stop words and Lemmatization {}".format(len(lemma_words)))
    print("Number of type with punctuation and removing stop words and Lemmatization {}".format(len(lemma_dist_tokens)))
    print("Top 10 Tokens with punctuation and removing stop words and Lemmatization: {}".format(stats6))

    print("\n")

def token_without_punctuation(words):
    stats = []
    stats2 = []
    stats3 = []
    stats4 = []
    stats5 = []
    stats6 = []
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in words]
    my_dict_stripped = {i: stripped.count(i) for i in stripped}
    b = list(zip(my_dict_stripped.values(), my_dict_stripped.keys()))
    b.sort(reverse = True)
    for i in range(1,11):
        stats.append(b[i])
    print("Number of tokens without punctuation {}".format(len(stripped)))
    print("Number of types without punctuation {}".format(len(b)))
    print("Top 10 Tokens without punctuation: {}".format(stats))
    print("****************Stemming****************")
    stem_words, stem_dist_tokens = stemming_words(stripped)
    stem_dist_tokens.sort(reverse=True)
    for i in range(1, 11):
        stats3.append(stem_dist_tokens[i])
    print("Number of Tokens without punctuation and stemming {}".format(len(stem_words)))
    print("Number of type without punctuation and stemming {}".format(len(stem_dist_tokens)))
    print("Top 10 Tokens without punctuation and stemming: {}".format(stats3))

    print("****************Lemmatization****************")
    lemma_words, lemma_dist_tokens = lemmatizing_words(stripped)
    lemma_dist_tokens.sort(reverse=True)
    for i in range(1, 11):
        stats5.append(lemma_dist_tokens[i])
    print("Number of Tokens without punctuation and Lemmatization {}".format(len(lemma_words)))
    print("Number of type without punctuation and Lemmatization {}".format(len(lemma_dist_tokens)))
    print("Top 10 Tokens without punctuation and Lemmatization: {}".format(stats5))
    c, stop_text = stopwords_removal(stripped)
    c.sort(reverse=True)
    for i in range(1, 11):
        stats2.append(c[i])
    print("****************Stop words Removed****************")
    print("Number of Tokens without punctuation and removing stop words {}".format(len(stop_text)))
    print("Number of type without punctuation and removing stop words {}".format(len(c)))
    print("Top 10 Tokens without punctuation and removing stop words: {}".format(stats2))
    print("****************Stemming****************")
    stem_words, stem_dist_tokens = stemming_words(stop_text)
    stem_dist_tokens.sort(reverse=True)
    for i in range(1, 11):
        stats4.append(stem_dist_tokens[i])
    print("Number of Tokens without punctuation and removing stop words and stemming {}".format(len(stem_words)))
    print("Number of type without punctuation and removing stop words and stemming {}".format(len(stem_dist_tokens)))
    print("Top 10 Tokens without punctuation and removing stop words and stemming: {}".format(stats4))
    print("****************Lemmatization****************")
    lemma_words, lemma_dist_tokens = lemmatizing_words(stop_text)
    lemma_dist_tokens.sort(reverse=True)
    for i in range(1, 11):
        stats6.append(lemma_dist_tokens[i])
    print("Number of Tokens without punctuation and removing stop words and Lemmatization {}".format(len(lemma_words)))
    print("Number of type without punctuation and removing stop words and Lemmatization {}".format(len(lemma_dist_tokens)))
    print("Top 10 Tokens without punctuation and removing stop words and Lemmatization: {}".format(stats6))
    print("\n")



load_data()
