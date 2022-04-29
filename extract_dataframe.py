import json
from bleach import clean
import pandas as pd
from textblob import TextBlob
import numpy as np
import re
import matplotlib.pyplot as plt
plt.style.use('fivethirtyeight')

# import zipfile

# with zipfile.ZipFile("./Data/Economic_Twitter_Data.zip", "r") as zip_ref:
#     zip_ref.extractall("./Data")
    
    
def read_json(json_file: str) -> list:
    """
    json file reader to open and read json files into a list
    Args:
    -----
    json_file: str - path of a json file

    Returns
    -------
    length of the json file and a list of json
    """

    tweets_data = []
    for tweets in open(json_file, 'r'):
        tweets_data.append(json.loads(tweets))

    return len(tweets_data), tweets_data



class TweetDfExtractor:
    """
    this function will parse tweets json into a pandas dataframe

    Return
    ------
    dataframe
    """

    def __init__(self, tweets):

        self.tweets = tweets

    # an example function
    def find_created_time(self) -> list:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        df['date'] = np.array([tweet.get('created_at') for tweet in self.tweets])
        # print(df['date'].head(3))
        return df['date']
    
    def find_source(self) -> list:
        df = pd.DataFrame(data=[tweet.get("source") for tweet in self.tweets], columns=['source'])
        # print(df)
        return df['source']

    def find_full_text(self) -> list:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        return df['Tweets']

    def clean_tweet(self):
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        cleanTweet = []
        for tweet in df['Tweets']:
            clean = ' '.join(re.sub("(@[A-Za-z0-9]+)|([^0-9A-Za-z \t])|(\w+:\/\/\S+)", " ", tweet).split())
            cleanTweet.append(clean)
        # print(cleanTweet[0:5]) 
        return cleanTweet

    def find_statuses_count(self) -> list:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        df['user'] = np.array([tweet.get('user') for tweet in self.tweets])
        df['statuses_count'] = np.array([hash.get('statuses_count') for hash in df['user']])
        # print(df['statuses_count'].head(3))
        return df['statuses_count']

    def find_sentiments(self):
        analysis = self.clean_tweet()
        # print(analysis)
        # df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        # df['sentiments'] = np.array([x for x in df['Tweets']])
        for analysis in analysis:
            polarity = str(TextBlob(analysis).sentiment.polarity)
            subjectivity = str(TextBlob(analysis).sentiment.subjectivity)
            return [polarity , subjectivity]
            # print(polarity , subjectivity)
    # def find_sentiments(self):
    #     analysis = self.clean_tweet()
    #     print(analysis)
    #     # df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
    #     # df['sentiments'] = np.array([x for x in df['Tweets']])
    #     for analysis in analysis:
    #         # print(TextBlob(analysis).sentiment.polarity)
    #         if TextBlob(analysis).sentiment.polarity > 0:
    #             return 1
    #         elif TextBlob(analysis).sentiment.polarity == 0:
    #             return 0
    #         else:
    #             return -1
        # return self.tweets_list[['polarity', 'subjectivity']]
    
    def find_lang(self) -> list:
        df = pd.DataFrame(data=[tweet.get("lang") for tweet in self.tweets], columns=['lang'])
        # print(df)
        return df['lang']
            

    def find_favourite_count(self) -> list:
        df = pd.DataFrame(data=[tweet.get("favorite_count") for tweet in self.tweets], columns=['likes'])
        # print(df)
        return df["likes"]    
    
    def find_retweet_count(self) -> list:
        df = pd.DataFrame(data=[tweet.get("retweet_count") for tweet in self.tweets], columns=['retweet'])
        # print(df)
        return df["retweet"]
    
        
    def find_screen_name(self) -> str:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        df['user'] = np.array([tweet.get('user') for tweet in self.tweets])
        df['screen_name'] = np.array([hash.get('screen_name') for hash in df['user']])   
        # print(df['screen_name'])
        return df['screen_name']
    
    def find_followers_count(self) -> list:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        df['user'] = np.array([tweet.get('user') for tweet in self.tweets])
        df['followers_count'] = np.array([hash.get('followers_count') for hash in df['user']]) 
        # print(df['followers_count'])
        return df['followers_count']
                    

    def find_friends_count(self) -> list:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        df['user'] = np.array([tweet.get('user') for tweet in self.tweets])
        df['friends_count'] = np.array([hash.get('friends_count') for hash in df['user']])
        # print(df['friends_count'])
        return df['friends_count']
          

    def is_sensitive(self) -> list:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        df['possibly_sensitive'] = np.array([tweet.get('possibly_sensitive') for tweet in self.tweets])
        try:
            is_sensitive = np.array([tweet.get('possibly_sensitive') for tweet in self.tweets])
        except KeyError:
            is_sensitive = None
        # print(df['possibly_sensitive'].head(2))
        # print(is_sensitive)
        return is_sensitive    

    def find_hashtags(self) -> list:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        df['entities'] = np.array([tweet.get('entities') for tweet in self.tweets])
        df['hashtags'] = np.array([hash.get('hashtags') for hash in df['entities']])
        # print(df['hashtags'].head(2))
        return df['hashtags']
    

    def find_mentions(self) -> list:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        df['entities'] = np.array([tweet.get('entities') for tweet in self.tweets])
        df['mentions'] = np.array([hash.get('user_mentions') for hash in df['entities']])
        # print(df['user_mentions'])
        return df['mentions']


    def find_location(self) -> list:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        df['user'] = np.array([tweet.get('user') for tweet in self.tweets])
        df['location'] = np.array([hash.get('location') for hash in df['user']])
        # print(df['location'].head(2))
        try:
            location = np.array([hash.get('location') for hash in df['user']])
        except TypeError:
            location = ''
        return location
    
    
    def get_tweet_df(self, save=False) -> pd.DataFrame:
        """required column to be generated you should be creative and add more features"""

        columns = ['created_at', 'source', 'original_text', 'polarity', 'subjectivity', 'lang', 'favorite_count',
                   'retweet_count',
                   'original_author', 'followers_count', 'friends_count', 'possibly_sensitive', 'hashtags',
                   'user_mentions', 'place']

        created_at = self.find_created_time()
        source = self.find_source()
        text = self.find_full_text()
        polarity, subjectivity = self.find_sentiments()
        lang = self.find_lang()
        fav_count = self.find_favourite_count()
        retweet_count = self.find_retweet_count()
        screen_name = self.find_screen_name()
        follower_count = self.find_followers_count()
        friends_count = self.find_friends_count()
        sensitivity = self.is_sensitive()
        hashtags = self.find_hashtags()
        mentions = self.find_mentions()
        location = self.find_location()
        data = zip(created_at, source, text, polarity, subjectivity, lang, fav_count, retweet_count, screen_name,
                   follower_count, friends_count, sensitivity, hashtags, mentions, location)
        df = pd.DataFrame(data=data, columns=columns)

        if save:
            df.to_csv('processed_tweet_data.csv', index=False)
            print('File Successfully Saved.!!!')

        return df

    
    def draw_plan(self) -> list:
        df = pd.DataFrame(data=[tweet.get("text") for tweet in self.tweets], columns=['Tweets'])
        df['id'] = np.array([tweet.get('id') for tweet in self.tweets])
        df['lang'] = np.array([tweet.get('lang') for tweet in self.tweets])
        df['likes'] = np.array([tweet.get('favorite_count') for tweet in self.tweets])
        df['reply'] = np.array([tweet.get('retweet_count') for tweet in self.tweets])
        df['date'] = np.array([tweet.get('created_at') for tweet in self.tweets])
        df['user'] = np.array([tweet.get('user') for tweet in self.tweets])
        df['entities'] = np.array([tweet.get('entities') for tweet in self.tweets])        
        df['hashtags'] = np.array([hash.get('hashtags') for hash in df['entities']])
        df['user'] = np.array([df])
        df['statuses_count'] = np.array([hash.get('statuses_count') for hash in df['user']])
        
        # print(df['statuses_count'].head(2))

        # print(df['text'])
        return df


if __name__ == "__main__":
    # columns = ['created_at', 'source', 'original_text', 'polarity', 'subjectivity', 'lang', 'favorite_count',
    #                'retweet_count',
    #                'original_author', 'followers_count', 'friends_count', 'possibly_sensitive', 'hashtags',
    #                'user_mentions', 'place']
    # required column to be generated you should be creative and add more features
    _, tweet_list = read_json("./data/Economic_Twitter_Data.json")
    tweets = tweet_list
    # TweetDfExtractor = TweetDfExtractor()
    tweet = TweetDfExtractor(tweets)
    # df = tweet.find_full_text()
    # # df = tweet.find_statuses_count()
    # df = tweet.find_created_time()
    # df = tweet.find_source()
    # df = tweet.find_lang()
    # df = tweet.find_favourite_count()
    # df = tweet.find_retweet_count()
    # df = tweet.find_screen_name()
    # df = tweet.find_followers_count()
    # df = tweet.find_friends_count()
    # df = tweet.is_sensitive()
    # df = tweet.find_hashtags()
    # df = tweet.find_mentions()
    # df = tweet.find_location()
    # # df = tweet.clean_tweet()
    # df = tweet.find_sentiments()
       
    tweet_df = tweet.get_tweet_df()


