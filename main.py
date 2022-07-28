import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

response = requests.get(URL)
web_page = response.text
soup = BeautifulSoup(web_page, "html.parser")

#print(soup.prettify())
handred_movies = soup.find_all(name="h3", class_="title")
with open ("movies.txt", "w", encoding='utf-8') as f:
    for movie in handred_movies[::-1]:

        f.write(movie.text + "\n")
        #print(movie.getText())
        print(movie.text)




