from bs4 import BeautifulSoup
import requests

# response = requests.get("https://news.ycombinator.com/news")
# response.raise_for_status()
# response = response.text
# # print(response)

# soup = BeautifulSoup(response, "html.parser")
# points = soup.select(".score")

# max_points = 0
# id = ""
# for point in points:
#   point_text = point.getText().split(" ")[0]
#   point_text = int(point_text.replace(",", ""))
#   if point_text > max_points:
#     max_points = point_text
#     id = point.get("id")[6:]


# stories = soup.select(".titleline")
# for story in stories:
#   story_id = story.parent.parent.get("id")
#   story_href = story.find("a").get("href")
#   if story_id == id:
#     print(story.getText())
#     print(story_href)



# with open("index.html") as fp:
#   contents = fp.read()

# soup = BeautifulSoup(contents, "html.parser")



URL = "https://www.complex.com/pop-culture/a/complex/movies-to-see-before-you-die"
movies_list = []

response = requests.get(URL)
response.raise_for_status()
response = response.text

soup = BeautifulSoup(response, "html.parser")
movies = soup.find_all(name="div", class_="subbuzz-wrapper")
for movie in movies:
  movie_title = movie.find(name="span", class_="js-subbuzz__title-text")
  if movie_title:
    movie_title = movie_title.getText()
    movies_list.append(movie_title)
movies_list[::-1]


with open("movies.txt", mode="w") as file:
  for movie in movies_list:
    file.write(f"{movie}\n")



# movies = soup.select(".subbuzz-wrapper ")
# for movie in movies:
#   movie_title = movie.select_one(".js-subbuzz__title-text")
#   if movie_title:
#     movie_title = movie_title.getText()
#     print(movie_title)

