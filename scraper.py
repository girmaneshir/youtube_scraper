import requests
from bs4 import BeautifulSoup
import re

def get_video_id(url):
    match = re.search(r'(?<=v=|/)([a-zA-Z0-9_-]{11})', url)
    return match.group(0) if match else None

def scrape_video_details(video_id):
    url = f'https://www.youtube.com/watch?v={video_id}'
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')

    title = soup.find('h1').text.strip()
    views = soup.find('span', class_='view-count').text.strip() if soup.find('span', class_='view-count') else "N/A"
    likes = soup.find('button', class_='style-default-size').text.strip() if soup.find('button', class_='style-default-size') else "N/A"
    comments = soup.find('h2', class_='count-text').text.strip() if soup.find('h2', class_='count-text') else "N/A"

    return {
        'Video Link': url,
        'Title': title,
        'Views': views,
        'Likes': likes,
        'Comments': comments,
        'Shares': "N/A",
        'Saves': "N/A"
    }