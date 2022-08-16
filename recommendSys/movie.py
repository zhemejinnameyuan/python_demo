import pandas as pd
import numpy as np
from math import *

source_data = pd.read_csv('data/movie.dat', sep=',')
lists = source_data.values.tolist()


movie_json = {}
for item in lists:
    title = item[1]
    tags = item[2].strip().split('|')
    movie_json[title] = tags


def Euclidean(title, title2):
    data1 = movie_json[title]
    data2 = movie_json[title2]
    distance = 0
    for key in data1:
        if key in data2:
            distance += 1

    return 1 / (1 + sqrt(distance))


def top10(movieTitle):
    res = []
    for title in movie_json.keys():
        if not title == movieTitle:
            simliar = Euclidean(movieTitle, title)
            res.append((title, simliar))
    res.sort(key=lambda x: x[1])
    return res[:10]


movieTitle = 'Jurassic World: Fallen Kingdom (2018)'
print(top10(movieTitle))
