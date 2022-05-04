# City data structure to store attributes
class City:
    # Constructor
    # lat / long won't be know until the API is called
    def __init__(self, name, state, lat=0.0, long=0.0):
        self.name = name
        self.state = state
        self.lat = lat
        self.long = long
