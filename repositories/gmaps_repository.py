import requests
from models.place import Place
from config import Config


class GMapsRepository:
    def __init__(self):
        self.api_key = Config.GOOGLE_MAPS_API_KEY
        self.headers = {
            'Content-Type': 'application/json',
            'X-Goog-Api-Key': self.api_key,
            'X-Goog-FieldMask': 'places.displayName,places.formattedAddress,places.priceLevel',
        }

    def search_places(self, query: str, limit: int = 10) -> list[Place]:
        url = "https://places.googleapis.com/v1/places:searchText"
        json_data = {
            'textQuery': query,
        }

        response = requests.post(url, json=json_data, headers=self.headers, timeout=10)
        response.raise_for_status()
        data = response.json()

        places = []
        for p in data.get("places", [])[:limit]:
            name = p.get("displayName")["text"]
            address = p.get("formattedAddress")
            rating = p.get("rating")
            directions_link = p.get("googleMapsUri")

            places.append(
                Place(
                    name=name,
                    address=address,
                    rating=rating,
                    directions_link=directions_link,
                )
            )
        return places
