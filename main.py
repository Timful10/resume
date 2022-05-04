from latlongapi import get_lat_long
from processor import read_cities_input
from processor import write_cities_output

# Another comments
if __name__ == '__main__':
    cities = read_cities_input('cities.csv')
    cities_output = []

    # Loop through the cities that were read in
    for c in cities:

        # Get the lat / long through the API
        cities_lat_long_api = get_lat_long(c)

        # There can be multiple lat / long for each City provided
        # Probably a better way of handling this as nested for loops aren't great
        for subcity in cities_lat_long_api:
            cities_output.append(subcity)

    # Write out the data
    write_cities_output(cities_output, "cities_output.csv")
