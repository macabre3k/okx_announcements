import sys
sys.path.append('./okx_announcements_downloader')

from okx_downloader.downloader import fetch_announcements

fetch_announcements(
    start_date="2025-01-01",
    end_date="2025-01-15",
    folder="./okx_announcements"
)
