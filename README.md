# Admin Panel Finder

## Author
G4UR4V007

## Version
1.0

## Description
The Admin Finder Tool is a Python script designed to find common admin panel URLs on a given website. It attempts to access these URLs and reports if any are found. Additionally, it containing a wordlist of unique words extracted from the website's content.

## Features
- Scans for common admin panel paths.
- Generates a wordlist from the website's content.
- Outputs found admin panel URLs and saves the wordlist to a file.

## Requirements
To run this tool, you need Python 3 and the following libraries:

- `requests`
- `beautifulsoup4`

## You can install the required libraries using pip:
- `pip install -r requirements.txt`

## Usage
- `python3 AdminFinder.py <domain>`
