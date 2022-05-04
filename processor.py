import csv

from city import City


def read_cities_input(filename):
    cities = []
    # Open file with read mode
    with open(filename, mode='r') as csv_file:
        csv_reader = csv.DictReader(csv_file)
        line_count = 0
        for row in csv_reader:
            if line_count == 0:
                # This is to show the headers of the csv
                # print(f'Column names are {", ".join(row)}')
                line_count += 1
            else:
                # Create variables of the name and state
                name = row["Name"]
                state = row["State"]

                # Create a City class instance
                city = City(name, state)

                # Append City to Cities Array
                cities.append(city)
    return cities


def write_cities_output(cities, filename):
    # Open csv in write mode
    with open(filename, mode='w') as cities_output_file:
        cities_writer = csv.writer(cities_output_file, lineterminator='\n', delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)

        for c in cities:
            cities_writer.writerow([c.name, c.state, c.lat, c.long])
