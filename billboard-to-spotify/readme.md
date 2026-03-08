# Billboard 100 → Spotify Playlist

Scrapes the Billboard Hot 100 chart for any date and creates a private Spotify playlist from the results.

## How It Works

1. Fetches the Billboard Hot 100 chart for a given date
2. Searches Spotify for each song
3. Creates a private playlist and adds all found tracks

## Setup

### 1. Install dependencies
```bash
pip install -r requirements.txt
```

### 2. Add Spotify credentials
In `main.py`, replace the placeholders with your credentials:
```python
client_id="YOUR-CLIENT-ID",
client_secret="YOUR-CLIENT-SECRET",
```

Get credentials by creating an app at [Spotify Developer Dashboard](https://developer.spotify.com/dashboard). Set the redirect URI to `http://example.com`.

## Usage

```bash
python main.py
```

When prompted, enter a date in `YYYY-MM-DD` format:
```
Which year do you want to travel to? Type the date in this format YYYY-MM-DD: 2005-08-12
```

A private Spotify playlist named `2005-08-12 Billboard 100` will be created in your account. Songs not found on Spotify are skipped with a notice.

## Notes

- On first run, a browser window will open for Spotify login. The auth token is cached in `token.txt`.
- Spotify search may not find every song — older or regional tracks are sometimes unavailable.