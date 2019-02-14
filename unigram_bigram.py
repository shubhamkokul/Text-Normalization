import nltk
import string
from nltk.util import ngrams
from collections import Counter
from nltk.corpus import stopwords



def load_data():
    stats = [];
    stats2 = []
    stats3 = [];
    stats4 = []
    stats5 = []
    stats6 = []
    stats7 = []
    stats8 = []
    stats9 = []
    stats10 = []
    stats11 = []
    stats12 = []
    filename = './data/data.txt' #change the filepath as per your reference.
    file = open(filename, 'r+')
    text = file.read()
    file.close()


    print("**************************************STATS WITH STOP WORDS**************************************")
    wordslower = nltk.word_tokenize(case_folding(text))
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in wordslower]
    unigrams = {i: stripped.count(i) for i in stripped}
    bigrams = ngrams(stripped, 2)
    print("Top 15 Unigrams with Stop Words")
    temp_dict_unigram = unigram_probability(unigrams,stripped)
    for i in range(0,16):
        stats.append(temp_dict_unigram[i])
    print(stats)
    print("Top 15 Bigrams with Stop Words")
    temp_dict_unigram = bigrams_probability(unigrams, bigrams)
    for i in range(0, 16):
        stats2.append(temp_dict_unigram[i])
    print(stats2)

    print("\n")
    print("**************************************STATS WITHOUT STOP WORDS**************************************")
    c, stop_text = stopwords_removal(wordslower)
    stripped = [w.translate(table) for w in stop_text]
    unigrams = {i: stripped.count(i) for i in stripped}
    bigrams = ngrams(stripped, 2)
    print("Top 15 Unigrams without Stop Words")
    temp_dict_unigram = unigram_probability(unigrams, stripped)
    for i in range(0, 16):
        stats3.append(temp_dict_unigram[i])
    print(stats3)
    print("Top 15 Bigrams without Stop Words")
    temp_dict_unigram = bigrams_probability(unigrams, bigrams)
    for i in range(0, 16):
        stats4.append(temp_dict_unigram[i])
    print(stats4)


    print("\n")
    print("**************************************STATS WITH STOP WORDS FIRST HALF**************************************")
    wordslower = nltk.word_tokenize(case_folding(text))
    B, C = wordslower[:len(wordslower)//2], wordslower[len(wordslower)//2:]
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in B]
    unigrams = {i: stripped.count(i) for i in stripped}
    bigrams = ngrams(stripped, 2)
    print("Top 15 Unigrams with Stop Words")
    temp_dict_unigram = unigram_probability(unigrams, stripped)
    for i in range(0, 16):
        stats5.append(temp_dict_unigram[i])
    print(stats5)
    print("Top 15 Bigrams with Stop Words")
    temp_dict_unigram = bigrams_probability(unigrams, bigrams)
    for i in range(0, 16):
        stats6.append(temp_dict_unigram[i])
    print(stats6)

    print("\n")
    print("**************************************STATS WITH STOP WORDS SECOND HALF**************************************")
    stripped = [w.translate(table) for w in C]
    unigrams = {i: stripped.count(i) for i in stripped}
    bigrams = ngrams(stripped, 2)
    print("Top 15 Unigrams with Stop Words")
    temp_dict_unigram = unigram_probability(unigrams, stripped)
    for i in range(0, 16):
        stats7.append(temp_dict_unigram[i])
    print(stats7)
    print("Top 15 Bigrams with Stop Words")
    temp_dict_unigram = bigrams_probability(unigrams, bigrams)
    for i in range(0, 16):
        stats8.append(temp_dict_unigram[i])
    print(stats8)

    print("\n")
    print(
        "**************************************STATS WITHOUT STOP WORDS FIRST HALF**************************************")
    wordslower = nltk.word_tokenize(case_folding(text))
    c, stop_text = stopwords_removal(wordslower)
    B, C = stop_text[:len(wordslower)//2], stop_text[len(wordslower)//2:]
    table = str.maketrans('', '', string.punctuation)
    stripped = [w.translate(table) for w in B]
    unigrams = {i: stripped.count(i) for i in stripped}
    bigrams = ngrams(stripped, 2)
    print("Top 15 Unigrams without Stop Words")
    temp_dict_unigram = unigram_probability(unigrams, stripped)
    for i in range(0, 16):
        stats9.append(temp_dict_unigram[i])
    print(stats9)
    print("Top 15 Bigrams without Stop Words")
    temp_dict_unigram = bigrams_probability(unigrams, bigrams)
    for i in range(0, 16):
        stats10.append(temp_dict_unigram[i])
    print(stats10)

    print("\n")
    print(
        "**************************************STATS WITHOUT STOP WORDS SECOND HALF**************************************")
    stripped = [w.translate(table) for w in C]
    unigrams = {i: stripped.count(i) for i in stripped}
    bigrams = ngrams(stripped, 2)
    print("Top 15 Unigrams without Stop Words")
    temp_dict_unigram = unigram_probability(unigrams, stripped)
    for i in range(0, 16):
        stats11.append(temp_dict_unigram[i])
    print(stats11)
    print("Top 15 Bigrams without Stop Words")
    temp_dict_unigram = bigrams_probability(unigrams, bigrams)
    for i in range(0, 16):
        stats12.append(temp_dict_unigram[i])
    print(stats12)

def stopwords_removal(words):
    stop_text = [];
    stop_words = set(stopwords.words('english'))
    for r in words:
        if not r in stop_words:
            stop_text.append(r)
    my_dict_stopword = {i: stop_text.count(i) for i in stop_text}
    c = list(zip(my_dict_stopword.values(), my_dict_stopword.keys()))
    return c, stop_text



def bigrams_probability(unigrams, bigrams):
    bigrams_total = {}
    temp = []
    temp2 = []
    s = Counter(bigrams)
    s1 = list(s.keys());
    for i in range(len(s1)):
        firstword, secondword = s1[i]
        cal = s.get(s1[i])/unigrams.get(firstword)
        if(cal == 1):
            temp2.append(cal)
        else:
            temp.append(cal)
    for j in range(len(temp)):
        bigrams_total.setdefault(str(s1[j]), temp[j])
    temp_dict = list(zip(bigrams_total.values(), bigrams_total.keys()))
    temp_dict.sort(reverse=True)
    return temp_dict


def unigram_probability(unigrams,token):
    unigrams_total = {}
    temp = []
    s = Counter(unigrams)
    s1 = list(s.keys())
    for i in range(len(s1)):
        temp.append(s.get(s1[i])/len(token))
    for j in range(len(temp)):
        unigrams_total.setdefault(str(s1[j]),temp[j])
    temp_dict = list(zip(unigrams_total.values(), unigrams_total.keys()))
    temp_dict.sort(reverse = True)
    return temp_dict


def case_folding(text):
    return text.lower()


load_data()
