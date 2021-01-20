#!/usr/bin/python3

import re
import json
import inflect
from flask import Flask, render_template, request

app = Flask(__name__)

punctuations = {}
number_converter = inflect.engine()

@app.route('/', methods=('GET', 'POST'))
def home():
    cosine_similarity = 0
    if request.method == 'POST':
        text1 = request.form['t1']
        text2 = request.form['t2']
        cosine_similarity = get_similarity(text1, text2)

    return render_template('Homepage.html',similarity=cosine_similarity*100)

def get_similarity(text1, text2):

    similarity = 0
    cosine_similarity = 0

    text1_list = text1.strip().replace(",","").replace(".","").split(" ")
    text2_list = text2.strip().replace(",","").replace(".","").split(" ")

    get_punctuations()

    text1_words = tokenize(text1_list)
    text2_words = tokenize(text2_list)

    word_set1 = set(text1_words)
    word_set2 = set(text2_words)
    
    all_words = word_set1.union(word_set2)
    
    common_words_in1 = [1 if word in word_set1 else 0 for word in all_words]
    common_words_in2 = [1 if word in word_set2 else 0 for word in all_words]
    
    for i in range(len(all_words)): 
        similarity+= common_words_in1[i]*common_words_in2[i] 
        cosine_similarity = similarity / float((sum(common_words_in1)*sum(common_words_in2))**0.5) 
    #print("similarity: ", cosine*100, "%")
    return cosine_similarity

def tokenize(text):
    tokens = []
    for sentence in text:
        words = sentence.lower()
        words = re.sub('@\S+', ' ', words)
        if "'" in words:
            words = omit_punctuations(words)
        match = re.match(r"([a-z]+)([0-9]+)", words , re.I)
        if match:
            words = number_converter.number_to_words(match.group(2))
            words += " "
            words += match.group(1)            
        words = re.findall('[A-Za-z]+', words)
        for word in words:
            tokens.append(word)
    return tokens

def get_punctuations():
    global punctuations
    with open('punctuations.json') as handler:
        punctuations = json.loads(handler.read())


def omit_punctuations(word):
    return punctuations[word]
#https://gist.github.com/nealrs/96342d8231b75cf4bb82    


if __name__ == "__main__":
    app.run(host = '0.0.0.0', port = 5001, debug=True)