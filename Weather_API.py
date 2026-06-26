from fastapi import FastAPI

app = FastAPI()

@app.get("/weather/{city}")
def get_weather(city : str):
    return {"City": city, "Weather": "Sunny", "Temperature": "30°C"}