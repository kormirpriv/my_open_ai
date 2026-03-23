from typing import Annotated

import requests

from my_open_ai.config import config

WEATHER_API_KEY = config.weather_api_key


def get_weather(
    city: Annotated[str, "Miasto, dla którego chcesz sprawdzić pogodę"]
) -> Annotated[
    str,
    "Miasto: ..., Temperatura: ... °C, Odczuwalna: ... °C, Pogoda: ..., Wilgotność: ... %",
]:
    if not city:
        return "Nie podałeś miasta"
    url = "https://api.openweathermap.org/data/2.5/weather"
    params = {"q": city, "appid": WEATHER_API_KEY, "units": "metric", "lang": "pl"}

    response = requests.get(url, params=params)
    data = response.json()

    if response.status_code != 200:
        return f"Błąd: {data.get('message', 'Nie udało się pobrać danych')}"
    result = "\n".join(
        [
            f"Miasto: {data['name']}",
            f"Temperatura: {data['main']['temp']}°C",
            f"Odczuwalna: {data['main']['feels_like']}°C",
            f"Pogoda: {data['weather'][0]['description']}",
            f"Wilgotność: {data['main']['humidity']}%",
        ]
    )

    return result
