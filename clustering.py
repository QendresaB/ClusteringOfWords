import matplotlib.pyplot as plt
import sys
import nltk
import csv
import re  # regular expression
import string

encodingTot = sys.stdout.encoding or 'utf-8'
from sklearn.cluster import KMeans
from sklearn.feature_extraction.text import TfidfVectorizer


def clean_tweets(tweet):
    stop_words = set(tweet.stopwords('english'))
    word_tokens = nltk.word_tokenize(tweet)
    # after tweepy preprocessing the colon symbol left remain after      #removing mentions
    tweet = re.sub(r':', '', tweet)
    # replace consecutive non-ASCII characters with a space
    tweet = re.sub(r'[^\x00-\x7F]+', '', tweet)
    # filter using NLTK library append it to a string
    filtered_tweet = [w for w in word_tokens if not w in stop_words]
    filtered_tweet = []
    # looping through conditions
    for w in word_tokens:
        # check tokens against stop words , emoticons and punctuations
        if w not in stop_words and w not in string.punctuation:
            filtered_tweet.append(w)
    return ' '.join(filtered_tweet)


regex_str = [

    r'<[^>]+>',  # HTML tags
    r'(?:@[\w_]+)',  # @-signs
    r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)",  # hash-tags
    r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+',  # URLs
    r'(?:(?:\d+,?)+(?:\.?\d+)?)',  # numbers
    r"(?:[a-z][a-z'\-_]+[a-z])",  # words with - and '
    r'(?:[\w_]+)'  # other words
]

# These Regex are used to EXCLUDE items from the text AFTER IMPORTING from csv with regex_str

numbers = r'(?:(?:\d+,?)+(?:\.?\d+)?)'
URL = r'http[s]?://(?:[a-z]|[0-9]|[$-_@.&+]|[!*\(\),]|(?:%[0-9a-f][0-9a-f]))+'
hash_tag = r"(?:\#+[\w_]+[\w\'_\-]*[\w_]+)"
at_sign = r'(?:@[\w_]+)'
dash_quote = r"(?:[a-z][a-z'\-_]+[a-z])"
html_tag = r'<[^>]+>'
other_word = r'(?:[\w_]+)'
other_stuff = r'(?:\S)'  # anything else - NOT USED
start_pound = r"([#?])(\w+)"  # Start with #
start_quest_pound = r"(?:^|\s)([#?])(\w+)"  # Start with ? or with #
cont_number = r'(\w*\d\w*)'  # Words containing numbers
slash_all = r'\s*(?:[\w_]*[/\\](?:[\w_]*[/\\])*[\w_]*)'
# Removes all words of 3 characters or less *****************************************************

short_words = r'\W*\b\w{1,3}\b'  # Short words of 3 character or less
short_wordsC = re.compile(short_words, re.VERBOSE | re.IGNORECASE)

# remove patterns matching url format
url_pattern = r'((http|ftp|https):\/\/)?[\w\-_]+(\.[\w\-_]+)+([\w\-\.,@?^=%&amp;:/~\+#]*[\w\-\@?^=%&amp;/~\+#])?'

# REGEX numbers, short words and URL only to EXCLUDE +++++++++++++++++++++++++++++++++++++++++++++++++++

num_url_short = r'(' + '|'.join([numbers, URL, short_words]) + ')'  # Exclude from tweets
comp_num_url_short = re.compile(num_url_short, re.VERBOSE | re.IGNORECASE)

with open("C:\Users\Admin\Desktop\IRAhandle_tweets_3.csv") as file:
    reader = csv.DictReader(file)
    count = 0
    data = {}
    for row in reader:
        for header, value in row.items():
            try:
                data[header].append(value)
            except KeyError:
                data[header] = [value]
    # extract the variables you want
    # author = data['airline_sentiment']
    # language = data['airline_sentiment']
    content = data['content']

tweet_clean_fin = []  # Cleaned Tweets - Final Version

txts = []
for tweet in content:
    tweet = re.sub(url_pattern, '', tweet)
    tweet = re.sub(html_tag, '', tweet)
    tweet = re.sub(start_quest_pound, '', tweet)
    tweet = re.sub(numbers, '', tweet)
    tweet = re.sub(cont_number, '', tweet)
    tweet = re.sub(slash_all, '', tweet)
    txts.append(tweet)


def remove_stop_words(entry_lst, stop_words_lst):
    return [word for word in entry_lst if word not in stop_words_lst]


vectorizier = TfidfVectorizer(strip_accents='ascii', stop_words='english', analyzer='word', max_df=0.6)
X = vectorizier.fit_transform(txts)

plt.plot()
distortions = []

K = range(1, 2)
for k in K:
    model = KMeans(n_clusters=k, init='k-means++', max_iter=200, n_init=5)
    model.fit(X)
    fitness = model.inertia_
    print("Fitness: " + str(fitness))
    distortions.append(fitness)

plt.plot(K, distortions, 'rx-')
plt.xlabel('The number of clusters')
plt.ylabel('Distortions')  # distortions
plt.title('Optimal number for clusters')
plt.show()

true_k = 10
model = KMeans(n_clusters=true_k, init='k-means++', max_iter=300)
model.fit(X)
print("Top terms per cluster:")
order_centroids = model.cluster_centers_.argsort()[:, ::-1]
terms = vectorizier.get_feature_names()
for i in range(true_k):
    print("Cluster %d:" % i),
    for ind in order_centroids[i, :10]:
        print(' %s' % terms[ind]),
    print

# def _limit_features(self, X, vocabulary, high=None, low=None,
# limit=None):

print("\n")
print("Ne cilin cluster ben pjese ky post:")
Y = vectorizier.transform(["Im voting for Donald Trump"])
prediction = model.predict(Y)
print("Ne cluster-in numer " + str(prediction))
print X

'''
Suggestions TODO:
0. Get the data from twitter (Twitter API)
1. do clusters with a random number from 1-10 
2. call the elbow function 
3. do as many clusters as suggested with the elbow
4. see the differences in the clusters
5. given a specific post see in each cluster it belongs to
6. generate a report in pdf for that
7. bonus: try to name the cluster
'''
