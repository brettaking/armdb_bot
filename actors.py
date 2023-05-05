from bs4 import BeautifulSoup
from requests import get
import re

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/70.0.3538.77 Safari/537.36'}

#movie_list = []

csv = []

#actor_list = ["Jeremy Renner"]

def get_filmography(actor):
    actor = actor.replace(" ", "%20")
    filmography = []
    url = ('https://www.rottentomatoes.com/search?search=' + actor)
    print(url)
    movies = get(url,headers = headers)
    movie_soup = BeautifulSoup(movies.content, 'html.parser')
    movie_list = movie_soup.find_all('search-page-media-row')
    for movie in movie_list:
        text = movie.get_text()
        filmography.append(text.strip())
    return filmography

#print(get_filmography("Jeremy Renner"))