from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import httpx
import os
from dotenv import load_dotenv

load_dotenv()

app = FastAPI()

API_KEY = os.getenv("OPENWEATHER_API_KEY")

class CityRequest(BaseModel):
    city: str

@app.post("/weather/")
async def get_weather(request: CityRequest):
    url = f"http://api.openweathermap.org/data/2.5/weather?q={request.city}&appid={API_KEY}&units=metric"
        

    async with httpx.AsyncClient() as client:
        response = await client.get(url)

    if response.status_code !=200:
        raise HTTPException(status_code=404, detail="City not found")
        
    data = response.json()
    weather = {
        "city": request.city,
        "temperature": f"{data['main']['temp']}ºC",
        "description": data["weather"][0]["description"]
    }
    return weather
