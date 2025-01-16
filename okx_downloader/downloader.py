import os
import requests
from bs4 import BeautifulSoup
from datetime import datetime
from .utils import validate_date_range, sanitize_filename, log_message

BASE_URL = "https://www.okx.com"
ANNOUNCEMENTS_PATH = "/help/category/announcements"
HEADERS = {"User-Agent": "Mozilla/5.0 (compatible; FetchBot/1.0)"}

def fetch_announcements(start_date: str, end_date: str, folder: str):
    validate_date_range(start_date, end_date)
    start_date = datetime.strptime(start_date, '%Y-%m-%d')
    end_date = datetime.strptime(end_date, '%Y-%m-%d')

    os.makedirs(folder, exist_ok=True)

    response = requests.get(f"{BASE_URL}{ANNOUNCEMENTS_PATH}", headers=HEADERS, timeout=10)
    if response.status_code != 200:
        log_message(f"Failed to fetch data from {BASE_URL}{ANNOUNCEMENTS_PATH}. Status code: {response.status_code}")
        return

    soup = BeautifulSoup(response.text, 'html.parser')
    announcements = soup.find_all('a', href=True)

    for announcement in announcements:
        link = announcement['href']
        title = announcement.get_text(strip=True)

        if not link.startswith('/help'):
            continue

        full_url = f"{BASE_URL}{link}"

        try:
            announcement_response = requests.get(full_url, headers=HEADERS, timeout=10)
            if announcement_response.status_code != 200:
                log_message(f"Failed to fetch announcement page: {full_url}. Status code: {announcement_response.status_code}")
                continue

            filename = sanitize_filename(f"{title}.html")
            file_path = os.path.join(folder, filename)

            with open(file_path, 'w', encoding='utf-8') as file:
                file.write(announcement_response.text)

            log_message(f"Saved: '{title}' to {file_path}")

        except requests.RequestException as e:
            log_message(f"Error fetching announcement {full_url}: {e}")
