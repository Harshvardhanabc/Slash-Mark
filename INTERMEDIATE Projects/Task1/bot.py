
# Meet SMC: your friend
# SMC stand for Slash Mark Chatbot

import nltk
import warnings

warnings.filterwarnings("ignore")
import numpy as np
import nltk
import random
import string  # to process standard python strings

# for reading text file
f = open('chatbot1.txt', 'r', errors='ignore')
m = open('chatbot2.txt', 'r', errors='ignore')
checkpoint = "./chatbot_weights.ckpt"

raw = f.read()
rawone = m.read()
raw = raw.lower()  # converts to lowercase
rawone = rawone.lower()  # converts to lowercase
nltk.download('punkt')  # first-time use only
nltk.download('wordnet')  # first-time use only
sent_tokens = nltk.sent_tokenize(raw)  # converts to list of sentences
word_tokens = nltk.word_tokenize(raw)  # converts to list of words
sent_tokensone = nltk.sent_tokenize(rawone)  # converts to list of sentences
word_tokensone = nltk.word_tokenize(rawone)  # converts to list of words

sent_tokens[:2]
sent_tokensone[:2]

word_tokens[:5]
word_tokensone[:5]

lemmer = nltk.stem.WordNetLemmatizer()


def LemTokens(tokens):
    return [lemmer.lemmatize(token) for token in tokens]


remove_punct_dict = dict((ord(punct), None) for punct in string.punctuation)


def LemNormalize(text):
    return LemTokens(nltk.word_tokenize(text.lower().translate(remove_punct_dict)))


Introduce_Ans = ["My name is SMC.", "My name is SMC you can called me Bro.", "Im SMC :) ",
                 "My name is SMC. and my nickname is Chatbot and i am happy to solve your queries :) "]
GREETING_INPUTS = ("hello", "hi", "hiii", "hii", "hiiii", "hiiii", "greetings", "sup", "what's up", "hey",)
GREETING_RESPONSES = ["hi", "hey", "hii there", "hi there", "hello", "I am glad! You are talking to me"]
Basic_Q = ("Tell me about SMC?", "Tell me about SMC", "tell me about SMC?", "Tell me about SMC","tell me about SMC")
Basic_Ans = ("SMC Stand for Slash Mark Chatbot.")

# Checking for greetings
def greeting(sentence):
    """If user's input is a greeting, return a greeting response"""
    for word in sentence.split():
        if word.lower() in GREETING_INPUTS:
            return random.choice(GREETING_RESPONSES)


# Checking for Basic_Q
def basic(sentence):
    for word in Basic_Q:
        if sentence.lower() == word:
            return Basic_Ans





# Checking for Introduce
def IntroduceMe(sentence):
    return random.choice(Introduce_Ans)


from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


# Generating response
def response(user_response):
    robo_response = ''
    sent_tokens.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokens)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokens[idx]
        return robo_response


# Generating response
def responseone(user_response):
    robo_response = ''
    sent_tokensone.append(user_response)
    TfidfVec = TfidfVectorizer(tokenizer=LemNormalize, stop_words='english')
    tfidf = TfidfVec.fit_transform(sent_tokensone)
    vals = cosine_similarity(tfidf[-1], tfidf)
    idx = vals.argsort()[0][-2]
    flat = vals.flatten()
    flat.sort()
    req_tfidf = flat[-2]
    if (req_tfidf == 0):
        robo_response = robo_response + "I am sorry! I don't understand you"
        return robo_response
    else:
        robo_response = robo_response + sent_tokensone[idx]
        return robo_response


def chat(user_response):
    user_response = user_response.lower()
    keyword = "SMC "
    keywordone = "SMC"
    keywordsecond = "SMC"

    if (user_response != 'bye'):
        if (user_response == 'thanks' or user_response == 'thank you'):
            flag = False
            print("SMC: You are welcome..")
            return "You are welcome.."
        else:
            if (user_response.find(keyword) != -1 or user_response.find(keywordone) != -1 or user_response.find(
                    keywordsecond) != -1):
                print("SMC: ",end="")
                print(responseone(user_response))
                return responseone(user_response)
                sent_tokensone.remove(user_response)
            elif (greeting(user_response) != None):
                print("SMC: "+greeting(user_response))
                return greeting(user_response)
            elif (user_response.find("your name") != -1 or user_response.find(" your name") != -1 or user_response.find(
                    "your name ") != -1 or user_response.find(" your name ") != -1):
                return IntroduceMe(user_response)
            elif (basic(user_response) != None):
                return basic(user_response)
            else:
                print("SMC: ",end="")
                print(response(user_response))
                return response(user_response)
                sent_tokens.remove(user_response)

    else:
        flag = False
        print("SMC: Bye! take care..")
        return "Bye! take care.."

