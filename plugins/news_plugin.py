import requests
import os

class NewsPlugin:
    def __init__(self):
        self.api_key = os.getenv("BING_API_KEY")
        self.endpoint = "https://api.bing.microsoft.com/"

        if not self.api_key:
            raise ValueError("BING_API_KEY is not set in the environment variables.")

    def get_latest_news(self, query):
        headers = {"Ocp-Apim-Subscription-Key": self.api_key}
        params = {"q": query, "count": 5}  # Fetch top 5 news articles
        response = requests.get(self.endpoint, headers=headers, params=params)
        
        if response.status_code == 200:
            data = response.json()
            return [article["name"] for article in data.get("value", [])]
        else:
            return [f"Error: Unable to fetch news (status code: {response.status_code})"]
