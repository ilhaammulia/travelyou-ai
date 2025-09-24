from repositories.gmaps_repository import GMapsRepository
from repositories.llm_repository import LLMRepository
import re


class SearchService:
    def __init__(self):
        self.llm_repo = LLMRepository()
        self.maps_repo = GMapsRepository()

    def search_places_from_prompt(self, prompt: str):
        llm_result = self.llm_repo.extract_query(prompt)
        places = self.__extract_places__(llm_result)

        result = []
        for place in places:
            data = self.maps_repo.search_places(place, 1)[0]
            result.append(data)

        return result

    def __extract_places__(self, content: str):
        names = []

        # 1. Bolded names: **Name**
        names += re.findall(r"\*\*(.*?)\*\*", content)

        # 2. Numbered list: "1. Name:" or "2. Name –"
        names += re.findall(r"\d+\.\s+([A-Z][\w\s\'\-&]+?)(?=[:\-])", content)

        # 3. Bulleted list: "* Name" or "- Name"
        names += re.findall(r"[\*\-]\s+([A-Z][\w\s\'\-&]+)", content)

        # Clean duplicates & strip spaces
        return list(set(name.strip() for name in names))