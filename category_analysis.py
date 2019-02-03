import csv
import pandas as pd

with open("master_data.csv") as file:
    csv_reader = csv.reader(file)
    next(file)
    data = list(csv_reader)
    i=0
    #categories: sad, happy, calm, angry
    sad_list = []
    happy_list = []
    calm_list = []
    angry_list = []
    for row in data:
        if row[10] == 'sad':
            sad_list.append(row)
        if row[10] == 'happy':
            happy_list.append(row)
        if row[10] == 'calm':
            calm_list.append(row)
        if row[10] == 'angry':
            angry_list.append(row)

#song_id,speechiness,instrumentalness,key,time signature,acousticness,danceability,energy,loudness,tempo,genre
#sad attributes
s_speechiness = 0
s_instrumentalness = 0
s_key = 0
s_time_signature = 0
s_acousticness = 0
s_danceability = 0
s_energy = 0
s_loudness = 0
s_tempo = 0

for i in range(len(sad_list)): 
    s_speechiness += float(sad_list[i][1])
    s_instrumentalness += float(sad_list[i][2])
    s_key += float(sad_list[i][3])
    s_time_signature += float(sad_list[i][4])
    s_acousticness += float(sad_list[i][5])
    s_danceability += float(sad_list[i][6])
    s_energy += float(sad_list[i][7])
    s_loudness += float(sad_list[i][8])
    s_tempo += float(sad_list[i][9])
s_final_speechiness = s_speechiness/len(sad_list)
s_final_instrumentalness = s_instrumentalness/len(sad_list)
s_final_key = (s_key/len(sad_list))/10
s_final_time_signature = (s_time_signature/len(sad_list))/10
s_final_acousticness = s_acousticness/len(sad_list)
s_final_danceability = s_danceability/len(sad_list)
s_final_energy = s_energy/len(sad_list)
s_final_loudness = (s_loudness/len(sad_list))/10
s_final_tempo = (s_tempo/len(sad_list))/100

final_sad_attributes = [s_final_speechiness,s_final_instrumentalness,s_final_key, s_final_time_signature, s_final_acousticness,s_final_danceability, s_final_energy, s_final_loudness, s_final_tempo]

#happy attributes
h_speechiness = 0
h_instrumentalness = 0
h_key = 0
h_time_signature = 0
h_acousticness = 0
h_danceability = 0
h_energy = 0
h_loudness = 0
h_tempo = 0

for i in range(len(happy_list)): 
    h_speechiness += float(happy_list[i][1])
    h_instrumentalness += float(happy_list[i][2])
    h_key += float(happy_list[i][3])
    h_time_signature += float(happy_list[i][4])
    h_acousticness += float(happy_list[i][5])
    h_danceability += float(happy_list[i][6])
    h_energy += float(happy_list[i][7])
    h_loudness += float(happy_list[i][8])
    h_tempo += float(happy_list[i][9])
h_final_speechiness = h_speechiness/len(happy_list)
h_final_instrumentalness = h_instrumentalness/len(happy_list)
h_final_key = (h_key/len(happy_list))/10
h_final_time_signature = (h_time_signature/len(happy_list))/10
h_final_acousticness = h_acousticness/len(happy_list)
h_final_danceability = h_danceability/len(happy_list)
h_final_energy = h_energy/len(happy_list)
h_final_loudness = (h_loudness/len(happy_list))/10
h_final_tempo = (h_tempo/len(happy_list))/100

final_happy_attributes = [h_final_speechiness,h_final_instrumentalness,h_final_key, h_final_time_signature, h_final_acousticness,h_final_danceability, h_final_energy, h_final_loudness, h_final_tempo]

#calm attributes
c_speechiness = 0
c_instrumentalness = 0
c_key = 0
c_time_signature = 0
c_acousticness = 0
c_danceability = 0
c_energy = 0
c_loudness = 0
c_tempo = 0

for i in range(len(calm_list)): 
    c_speechiness += float(calm_list[i][1])
    c_instrumentalness += float(calm_list[i][2])
    c_key += float(calm_list[i][3])
    c_time_signature += float(calm_list[i][4])
    c_acousticness += float(calm_list[i][5])
    c_danceability += float(calm_list[i][6])
    c_energy += float(calm_list[i][7])
    c_loudness += float(calm_list[i][8])
    c_tempo += float(calm_list[i][9])
c_final_speechiness = c_speechiness/len(calm_list)
c_final_instrumentalness = c_instrumentalness/len(calm_list)
c_final_key = (c_key/len(calm_list))/10
c_final_time_signature = (c_time_signature/len(calm_list))/10
c_final_acousticness = c_acousticness/len(calm_list)
c_final_danceability = c_danceability/len(calm_list)
c_final_energy = c_energy/len(calm_list)
c_final_loudness = (c_loudness/len(calm_list))/10
c_final_tempo = (c_tempo/len(calm_list))/100

final_calm_attributes = [c_final_speechiness,c_final_instrumentalness,c_final_key, c_final_time_signature, c_final_acousticness,c_final_danceability, c_final_energy, c_final_loudness, c_final_tempo]

#angry attributes
a_speechiness = 0
a_instrumentalness = 0
a_key = 0
a_time_signature = 0
a_acousticness = 0
a_danceability = 0
a_energy = 0
a_loudness = 0
a_tempo = 0

for i in range(len(angry_list)): 
    a_speechiness += float(angry_list[i][1])
    a_instrumentalness += float(angry_list[i][2])
    a_key += float(angry_list[i][3])
    a_time_signature += float(angry_list[i][4])
    a_acousticness += float(angry_list[i][5])
    a_danceability += float(angry_list[i][6])
    a_energy += float(angry_list[i][7])
    a_loudness += float(angry_list[i][8])
    a_tempo += float(angry_list[i][9])
a_final_speechiness = a_speechiness/len(angry_list)
a_final_instrumentalness = a_instrumentalness/len(angry_list)
a_final_key = (a_key/len(angry_list))/10
a_final_time_signature = (a_time_signature/len(angry_list))/10
a_final_acousticness = a_acousticness/len(angry_list)
a_final_danceability = a_danceability/len(angry_list)
a_final_energy = a_energy/len(angry_list)
a_final_loudness = (a_loudness/len(angry_list))/10
a_final_tempo = (a_tempo/len(angry_list))/100

final_angry_attributes = [a_final_speechiness,a_final_instrumentalness,a_final_key, a_final_time_signature, a_final_acousticness,a_final_danceability, a_final_energy, a_final_loudness, a_final_tempo]
print(final_happy_attributes)
print(final_sad_attributes)
print(final_calm_attributes)
print(final_angry_attributes)
final_attributes =[final_happy_attributes, final_sad_attributes, final_calm_attributes,final_angry_attributes]

import plotly.plotly as py
import plotly.graph_objs as go

angry = go.Scatter(
    x=['speechiness', 'instrumentalness','key','time signature', 'acousticness','danceability','energy','loudness','tempo'],
    y= final_angry_attributes
)
calm = go.Scatter(
    x=['speechiness', 'instrumentalness','key','time signature', 'acousticness','danceability','energy','loudness','tempo'],
    y= final_calm_attributes
)
happy = go.Scatter(
    x=['speechiness', 'instrumentalness','key','time signature', 'acousticness','danceability','energy','loudness','tempo'],
    y= final_happy_attributes
)
sad = go.Scatter(
    x=['speechiness', 'instrumentalness','key','time signature', 'acousticness','danceability','energy','loudness','tempo'],
    y= final_sad_attributes
)
data = [angry, calm, happy,sad]

py.plot(data, filename = 'basic-line', auto_open=True)



