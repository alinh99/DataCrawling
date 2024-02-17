from bs4 import BeautifulSoup
import requests
import pandas as pd

def get_data(url):
    url_request = requests.get(url)
    return url_request.text

city_result = {}  # Initialize an empty dictionary for city results

soup = BeautifulSoup(get_data("https://www.gov.uk/government/publications/list-of-cities/list-of-cities-html"), "html.parser")

# Open the CSV file once before the loop starts
with open("england_city.csv", "w") as file:
    file.write("name\n")  # Write header


city_names = list(soup.find("h4", {"id": "england"}).find_next().descendants)

cities = []

for city_name in city_names:
    city = city_name.text
    if '\n' in city_name:
        continue
    if '*' in city:
        city = city.replace("*", "")
    city_result = {"name": city}
    cities.append(city_result)

df = pd.DataFrame(cities)
df.drop_duplicates(inplace=True)
df.to_csv("england_city.csv", mode='a', header=False, index=False)