import os
import requests
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

def fetch_serper_news(query: str) -> dict:
    """Fetch raw Serper search results for a given query (synchronously)."""
    print(f"Fetching news for query: {query}")
    
    # Check if API key is available
    api_key = os.getenv("SERPER_API_KEY")
    if not api_key:
        return {"error": "SERPER_API_KEY environment variable is not set"}
    
    url = "https://google.serper.dev/search"
    headers = {
        "X-API-KEY": api_key,
        "Content-Type": "application/json"
    }
    payload = {"q": query, "num": 8}

    try:
        response = requests.post(url, json=payload, headers=headers)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        return {"error": str(e)}

def main():
    data = fetch_serper_news("AI news")
    print(data)

if __name__ == "__main__":
    main()
