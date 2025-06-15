#  Async Weather API

This is a simple **FastAPI** project that uses **async/await** and **OpenWeatherMap API** to fetch weather data for a given city.

##  Features ##
- Built with FastAPI
- Uses async `httpx` for non-blocking API calls
- Reads secret API key from `.env` file
- Returns live weather data as JSON

##  Requirements ##

- Python 3.10+
- fastapi
- httpx
- python-dotenv
- uvicorn

Install with:

```bash
pip install -r requirements.txt
