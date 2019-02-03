import requests
from flask import Flask, request

app = Flask(__name__)

mood = None
@app.route('/quiz', methods=['POST'])
def quiz():
    if request.method == 'POST':
        key = request.get_json()
        print (key)
        mood = key
    return key

@app.route("/relaxnation/")#, method='POST')
def home():

    return requests.get('http://andrewsimonds14.github.io/').content

@app.route("/post")
def post():
    return "TEST"

#key = quiz()

# coding: utf-8

# In[14]:


#Classify songs as happy, sad, angry, or calm

#Make 5 separate decision trees, trained with 5 separate data sets
#Run predicitons through every decision tree, take most popular response
#combination of decision trees improves accuracy

from sklearn import tree
from sklearn.externals import joblib
import pandas as pd
from spotify_api_client import search, search_all, get

classifier = joblib.load("best_classifier.joblib")



#Accept a genre from the website, return a song ID that will interest the listener

#import necessary libraries
from sklearn import tree
from sklearn.externals import joblib
import pandas as pd
import numpy as np
import random
from spotify_api_client import search, search_all, get

#import the trained classifier
classifier = joblib.load("best_classifier.joblib")


# In[33]:


#use clf2 to accept a genre as input, check the new songs playlist
#on spotify for songs with matching genre, return song ID

def get_track(genre, tree):
    genre = str(genre)
    proceed = True
    pl_list = ['new music friday', 'singled out', 'new music friday uk',
               'new music friday canada', 'new music friday au']
    rand_int = random.randint(0,4)
    #goes to 'new music friday' playlist which is updated by spotify
    print(rand_int)
    print(f"the playlist: {pl_list[rand_int]}")

    playlist_id = search(pl_list[rand_int], 'playlist') #returns id of first search result in a string
    playlist_data = get(f'v1/playlists/{playlist_id}/tracks') #array of song data

    num_array = np.linspace(0,98, 99)
    int_array = [ int(x) for x in num_array]

    while proceed == True:

        index = random.randint(0, len(int_array)-1)
        n = int_array[index]
        print(index, n)

        track_id = playlist_data['items'][n]['track']['id']
        try:
            track_data = get(f'v1/audio-features/{track_id}')

            key = track_data['key']
            time_sig = track_data['time_signature']
            acst = track_data['acousticness']
            dance = track_data['danceability']
            enrg = track_data['energy']
            loud = track_data['loudness']
            tempo = track_data['tempo']
            speech = track_data['speechiness']
            instrum = track_data['instrumentalness']

            track_features = [speech, instrum, key, time_sig, acst, dance, enrg, loud, tempo]
            #print(track_features)

            result = tree.predict([track_features])
            #print(result)

        except:
            result = 'invalid'
            #print(result)

        int_array = np.delete(int_array, index)
        print(result, track_id)

        if result == genre:
            print("hello")
            return f'https://open.spotify.com/embed/track/{track_id}'
            break


# In[34]:


track = get_track(mood, classifier)
quiz = open("quiz.html").read().format(track=track)


# In[ ]:





# In[ ]:
