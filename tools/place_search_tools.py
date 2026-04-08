import os
from utils.place_info_search import GooglePlaceSearchTool, TavilyPlaceSearchTool
from typing import List
from langchain.tools import tool
from dotenv import load_dotenv


class PlaceSearchTool:
    def __init__(self):
        load_dotenv()
        self.google_api_key = os.environ.get('GPLACES_API_KEY')
        self.google_places_search = GooglePlaceSearchTool(self.google_api_key)
        self.tavily_search = TavilyPlaceSearchTool()
        self.place_search_tool_list = self._setup_tool()

    def _setup_tool(self) -> List:
        """Setup all the tool for the place search tool"""

        @tool
        def search_attractions(place: str) -> str:
            """Search attractions of a place"""
            try:
                attraction_result = self.google_places_search.google_search_attractions(place)
                if attraction_result:
                    return f"Following are the attractions of {place} as suggested by google: {attraction_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_attractions(place)
                return f"Google cannot find the attraction due to {e}.\nFollowing are the attractions of {place} as suggested by Tavily: {tavily_result}"
            
        @tool
        def search_restaurants(place: str) -> str:
            """Search restaurants of a place"""
            try:
                restaurants_result = self.google_places_search.google_search_restaurants(place)
                if restaurants_result:
                    return f"Following are the restaurants found by Google for {place}.\nThe restaurants: {restaurants_result}"
                else:
                    tavily_restaurants = self.tavily_search.tavily_search_restaurants(place)
                    return f"Following are the restaurants found by Tavily for {place}.\nThe restaurants: {tavily_restaurants}"
            except Exception as e:
                raise f"{ValueError} no restaurant is found for {place} due to {e}"
            
        @tool
        def search_activities(place:str) -> str:
            """Search activities of a place"""
            try:
                restaurants_result = self.google_places_search.google_search_activity(place)
                if restaurants_result:
                    return f"Following are the activities in and around {place} as suggested by google: {restaurants_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_activity(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the activities of {place}: {tavily_result}"  ## Fallback search using tavily in case google places fail
        
        @tool
        def search_transportation(place:str) -> str:
            """Search transportation of a place"""
            try:
                restaurants_result = self.google_places_search.google_search_transportation(place)
                if restaurants_result:
                    return f"Following are the modes of transportation available in {place} as suggested by google: {restaurants_result}"
            except Exception as e:
                tavily_result = self.tavily_search.tavily_search_transportation(place)
                return f"Google cannot find the details due to {e}. \nFollowing are the modes of transportation available in {place}: {tavily_result}"  ## Fallback search using tavily in case google places fail
        
        return [search_attractions, search_restaurants, search_activities, search_transportation]   