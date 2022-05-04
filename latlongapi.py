import requests
import urllib.parse

from city import City


def get_lat_long(city):
    cities = []
    # Get Lat / Long for a given city
    address = city.name + "," + city.state
    url = 'https://nominatim.openstreetmap.org/search/' + urllib.parse.quote(address) + '?format=json'

    # Get the response from the API
    response = requests.get(url).json()

    # Iterate through the response to get all the lat / longs
    for r in response:
        lat = r["lat"]
        long = r["lon"]
        city = City(city.name, city.state, lat, long)
        cities.append(city)
    return cities
