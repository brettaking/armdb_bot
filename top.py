#/usr/bin/python3
import csv
import re
import gspread
from oauth2client.service_account import ServiceAccountCredentials
import time
from collections import Counter


"""USe oauth2client and gspread to open Google Sheets spreadsheet"""
# use creds to create a client to interact with the Google Drive API
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = ServiceAccountCredentials.from_json_keyfile_name('client_secret.json', scope)
gclient = gspread.authorize(creds)

# Find a workbook by name and open the correct worksheet
sheet = gclient.open_by_key('1ksz8yZgNZKGfxQpqpgyITwHRqovxbS7LMsDDdweFo98')
worksheet = sheet.worksheet('Text Actor List Sheet')

values = worksheet.get_all_values()

class Movie:
    def __init__(self, index, title, imdb, cast_list):
        self.index = index
        self.title = title
        self.imdb = imdb
        self.cast_list = cast_list
        
    def print_title(self):
        return self.title
        
    def display(self):
        return (self.index,self.title,self.imdb,self.cast_list)
        
    def castlist(self):
        return self.cast_list
        
    def in_movie(self, actor):
        for i in self.cast_list:
                  return self.title
                 
    def in_movie_bool(self, actor):
        for i in self.cast_list:
            if actor == i:
                return True


movie_objects = []
for i in values:
    cast_list = []
    for j in range(3,(len(i))):
        if (i[j] != "Loading..." and i[j] !="#N/A" and i[j] !=""):
            cast_list.append(i[j])
    movie_objects.append(Movie(i[0],i[1],i[2],cast_list))
        

def create_actor_list():    
    actor_list = []    
    for obj in movie_objects:
        for i in obj.castlist():
            actor_list.append(i)
    return actor_list
    
def create_count_list(num):
    actor_list = create_actor_list()
    actor_count = Counter(actor_list)
    count_list = zip(actor_count.keys(), actor_count.values())
    count_list = list(count_list)
    count_list.sort(key=lambda a:a[1], reverse=True)
    count_list = count_list[:num]
    return count_list
    

def in_movie_check(actor):
    movies = []
    for obj in movie_objects:
        if (obj.in_movie_bool(actor)):
            movies.append((obj.in_movie(actor)))
    return movies 

def actor_compare(actor1,actor2):
    movies_in_common = []
    movies1 = in_movie_check(actor1)
    movies2 = in_movie_check(actor2)
    for movie1 in movies1:
        for movie2 in movies2:
            if movie1 == movie2:
                movies_in_common.append(movie1)
    return movies_in_common
        
def all_titles():
    for obj in movie_objects:
        print (obj.print_title())
        
def all_display():
    for obj in movie_objects:
        print (obj.display())
        
def get_castlist(movie):
    for obj in movie_objects:
        if movie == obj.title:
            return obj.castlist()
