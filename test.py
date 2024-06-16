import pandas as pd
import requests
from bs4 import BeautifulSoup
def f1():
    data = {
        'X': ['a', 'b', 'c'],
        'Y': ['d', 'e', 'f'],
        'Z': ['g', 'h', 'i'],
        'W': ['j', 'k', 'l']
    }
    df = pd.DataFrame(data)
    print(df)

    m = df.iloc[:,1:2]
    print(m)

    n = df.iloc[1:,:]
    print(n)


# 2


def req1():
    import requests

    url = "https://api.themoviedb.org/3/trending/movie/day?language=en-US"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YTVhNGJiMGJmMjNlMjVhYWViMGM4YjkxNzMzOGRiNiIsInN1YiI6IjY1OGQ2NmNjYTMzNjEyNWI5OTU4ZWVhMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zbsRu4BHilwxZ-7j7xAa6NBIboZOowq2x68puP1LxSg"
    }

    response = requests.get(url, headers=headers)

    print(response.text)

def f2():
    import requests

    url = "https://api.themoviedb.org/3/account/20870147/rated/movies?language=en-US&page=1&sort_by=created_at.asc"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiI4YTVhNGJiMGJmMjNlMjVhYWViMGM4YjkxNzMzOGRiNiIsInN1YiI6IjY1OGQ2NmNjYTMzNjEyNWI5OTU4ZWVhMyIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.zbsRu4BHilwxZ-7j7xAa6NBIboZOowq2x68puP1LxSg"
    }

    response = requests.get(url, headers=headers)

    print(response.text)



import requests
headers = {
  'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}

response = requests.get(f'https://www.ambitionbox.com/list-of-companies?page=2', headers=headers)
print(response.text)
