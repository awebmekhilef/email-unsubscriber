# Email unsubscriber
Scrapes your email threads to open all unsubscribe links and press them.

## Setup
### Get and API credentials
1. Follow [this guide](https://developers.google.com/workspace/guides/enable-apis) to create a Google Cloud project and enable the Gmail API.
2. Download the credentials and save them in the root directory under the name `credentials.json`.
3. For testing purposes add the email address you'd like to run this script for to "OAuth consent screen/Test users".

### Usage
1. (Optional) Initialize a virtual environment using: `python3 -m venv .venv`
2. Run: `pip install -r requirements.txt`
3. Run: `python3 autounsub.py <max-emails>`
