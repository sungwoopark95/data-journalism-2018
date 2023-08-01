"""300초(5분) 동안 특정 키워드에 대한 Tweet을 수집하는 프로그램"""
import tweepy
import time

# OAuth Setup
consumer_key = 'iK6PbwIWdtHJ3VQ2Ba19PZMnQ'
consumer_secret = 'SeGZVqjzRYd3FGHW7VOFUeSihAJHmTvl5tYse8gVpN6fAX21uJ'
access_token = '923096752223219712-QaBkvj6hdMYmuZuzTKWjaRtPJHGqj8o'
access_secret = 'WckTNx5CbOeIDvlImae5LCTW46XJ4tf7shtfbArNbW1Dc'

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_secret)

# api Setup
api = tweepy.API(auth)

# making StreamListener Class
class MyListener(tweepy.StreamListener):
    def __init__(self, time_limit=60):
        self.start_time = time.time()
        self.limit = time_limit
        self.saveFile = open('twitter_file.txt', 'w', encoding='utf8')
        super(MyListener, self).__init__()

    def on_status(self, data):
        if (time.time() - self.start_time) < self.limit:
            self.saveFile.write(data.text)
            return True
        else:
            self.saveFile.close()
            return False

# making Streaming Object
twitter_stream = tweepy.Stream(auth, MyListener(time_limit=300))

# Starting Streaming
twitter_stream.filter(track=['이재명'])