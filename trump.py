import tweepy #pip install tweepy
import pandas as pd #pip install pandas
from IPython.display import display, HTML #part of the pandas library
import numpy as np #pip install numpy
from textblob import TextBlob #pip install TextBlob
import re #pip install re
import nltk #pip install nltk


#I have currently put in a variety of language analysis packages I found in python and implemented a data base in
#from the pandas package. I would like to implement a few other packages and algorithms for anaylsis. I am
#somewhat happy with how it looks now as a starting point. Obviously, it could do alot more, but I was hoping you might
#have some ideas as well. I have included instructions for how to download all of the external libraries I used so
#you should be able to run the code. Additionally, hard code to run every major method is present at the end of the
#file, but commented out and every method is commented with an explanation of what to do.

#As far as future plans go, I atleast want to implement the numpy package to visulalize our findings and then
#write a readme for this that explains any significant findings we found and the visualizations we have. I
#feel this has potential as a data science style research project or anaylsis more so that a software, although
#it can easily be generalized to any user outside of trump and expanded upon

#anyways, Ive typed far too much. PLEASE change this as much as you want and use any and all libraries you want to.
#Dont worry about messing it up or adding in pointless features. Just do whatever you think is a good idea and message
#me with any questions.



#returns the api linked to my twitter account that is used by tweepy
def getAPI():
    consumer_key = 'QYhsKGHC0Y28jClii5c3cfoXw'
    consumer_secret = 'lhHAfbDeT7vHIYLjSCcS9us1ZwQnXUyzoPS9XEzfLLJme2vPmi'
    access_token = '4166148659-vMBj0tCQgE0xPnRKBHq58FF3FArdYmdtE9ywzyG'
    access_token_secret = 'fj2NEXyDoM47WUpUKv9nfXskSCTk86BEfllh4DPvoevH0'
    # OAuth process, using the keys and tokens
    auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
    auth.set_access_token(access_token, access_token_secret)
    # Creation of the actual interface, using authentication
    api = tweepy.API(auth)
    return api

#prints data for how objective trumps tweets are
def objectiveAnaylsis(tweets):
    objective = []
    subjective = []
    for tweet in tweets:
        blob = TextBlob(tweet.text)
        if blob.sentiment.subjectivity > .5:
            subjective.append(tweet.text)
        else:
            objective.append(tweet.text)
    print(len(subjective)/len(tweets)*100, " % of tweets are subjective. ")
    print(len(objective)/len(tweets)*100, " % of tweets are objective. ")

#prints data for how polar the tweets trump sends out are
def polarAnalysis(tweets):
    polar = []
    notPolar = []
    for tweet in tweets:
        blob = TextBlob(tweet.text)
        if blob.sentiment.polarity > .5:
            polar.append(tweet.text)
        else:
            notPolar.append(tweet.text)
    print(len(polar)/len(tweets)*100, " % of tweets are polar")
    print(len(notPolar)/ len(tweets) * 100, " % of tweets are not polar")

#creates a data base that displays the all the data from the tweets in a table
#and displays it
def createDatabase(tweets):
    data = pd.DataFrame(data=[tweet.text for tweet in tweets], columns=['Tweets'])
    data['len'] = np.array([len(tweet.text) for tweet in tweets])
    data['ID'] = np.array([tweet.id for tweet in tweets])
    data['Date'] = np.array([tweet.created_at for tweet in tweets])
    data['Source'] = np.array([tweet.source for tweet in tweets])
    data['Likes'] = np.array([tweet.favorite_count for tweet in tweets])
    data['RTs'] = np.array([tweet.retweet_count for tweet in tweets])
    # We display the first 10 elements of the dataframe:
    display(data.head(10))
    return data

#returns a list of all of the tweets pulled from the get request
def getTweets(screenName, numberOfTweets, api):
    tweets = api.user_timeline(screen_name=screenName, count=numberOfTweets)
    return tweets

#stores all of the text from the tweets into one long string that can be analyzed easier than
#tweet objects
def getFullString(tweets):
    totalWords = ""
    for tweet in tweets:
        totalWords = totalWords + tweet.text
    return totalWords

#returns a list of every word from all the tweets in the list tweets
def getWordList(tweets):
    totalWords = ""
    for tweet in tweets:
        totalWords = totalWords + tweet.text
    totalWords.split()
    return totalWords

#prints the frequencies of the words in all of the tweets and then returns the dictionary that
#holds the frequencies
def getFrequencies(tweets):
    frequency = {}
    text_string = getFullString(tweets).lower()
    match_pattern = re.findall(r'\b[a-z]{3,15}\b', text_string)

    for word in match_pattern:
        count = frequency.get(word, 0)
        frequency[word] = count + 1

    frequency_list = frequency.keys()

    for words in frequency_list:
        print(words, frequency[words])
    return frequency

#returns tokens that label the part of speech for a single tweet
#this is mainly something I put in for myself, it uses alot of linguistics
#terminology that I learned about in my linguistics class and thought it
#was a cool application
def tokenize(tweet):
    tknzr = nltk.TweetTokenizer()
    s = str(tweet.text)
    return tknzr.tokenize(s)


api = getAPI() #runs the get api method
tweets = getTweets("realDonaldTrump", 200, api) #gets the most recent 200 tweets of donald trump
#createDatabase(tweets) #runs the database function
#subjectiveAnalysis(tweets) #runs subjective analysis
#polarAnaylsis(tweets) #runs objective analysis
#getWordList(tweets) #runs the get word list method
#getFrequencies(tweets) #runs the get frequencies method



















