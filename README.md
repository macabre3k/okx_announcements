# OKX Announcements Downloader

## Description
A tool to fetch and save announcements from the OKX website within a specified date range. The fetched announcements are saved as HTML files in a local folder for offline access and further analysis.

## Features
- Fetch announcements from the OKX website.
- Filter announcements by a specified date range.
- Save announcements as HTML files in a local folder.
- Modular design for easy extension and maintenance.

## Installation

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Steps
1. Clone the repository:
   ```bash
   git clone https://github.com/macabre3k/okx_announcements.git
   cd okx_announcements_downloader
   ```
2. Install the package:
   ```bash
   pip install -r requirements.txt
   ```
## Usage

### Example
```python
from okx_downloader.downloader import fetch_announcements

fetch_announcements(
    start_date="2023-01-01",
    end_date="2023-12-31",
    folder="./okx_announcements"
)
```
This will fetch all announcements from January 1, 2023, to December 31, 2023, and save them in the `./okx_announcements` folder.

### Command-line Usage
Coming soon.

## Development

### Installing Dependencies
Install the required dependencies using pip:
```bash
pip install -r requirements.txt
```

### Running Tests
To ensure everything works correctly, run the test suite:
```bash
python -m unittest discover -s tests
```

## Project Structure
```
okx_announcements_downloader/
├── okx_downloader/          # Main module
│   ├── __init__.py
│   ├── downloader.py        # Core logic
│   ├── utils.py        # Helper functions
├── requirements.txt         # Dependencies
├── setup.py                 # Package configuration
├── main.py         #Example
├── README.md                # Project documentation
├── DEPLOYMENT_GUIDE.md      # # Remote Server Deployment: Issues and Solutions
└── .gitignore               # Ignored files for Git

```

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contact
For questions or support, please contact [lesovaya.mary@mail.ru].
