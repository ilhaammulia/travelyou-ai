
class Place:
    def __init__(self, name, address=None, rating=None, directions_link=None):
        self.name = name
        self.address = address
        self.rating = rating
        self.directions_link = directions_link

    def to_dict(self):
        return {
            "name": self.name,
            "address": self.address,
            "rating": self.rating,
            "directions_link": self.directions_link,
        }
