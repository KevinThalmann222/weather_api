"""author: kevin thalmann."""

import requests


def get_current_weather(city: str = "Braunschweig, DE") -> str:
    """Ruft das aktuelle Wetter für eine bestimmte Stadt ab.

    Parameters:
        city (str): Der Name der Stadt. Standardmäßig ist es "Braunschweig".

    Returns:
        str: Eine Zeichenfolge, die das aktuelle Wetter für die angegebene Stadt enthält.
    """
    api_key = "bd268b483dc59a8cfa557f0f83ad7cf3"
    url = f"http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric"

    try:
        response = requests.get(url)
        data = response.json()
        if response.status_code == 200:
            weather_description = data["weather"][0]["description"]
            temperature = data["main"]["temp"]
            humidity = data["main"]["humidity"]
            wind_speed = data["wind"]["speed"]
            return f"Aktuelles Wetter in {city}: {weather_description}. Temperatur: {temperature}°C. Luftfeuchtigkeit: {humidity}%. Windgeschwindigkeit: {wind_speed} m/s."
        return f"Fehler beim Abrufen des Wetters für {city}."

    except Exception as e:
        return f"Fehler: {str(e)}"


if __name__ == "__main__":
    print(get_current_weather())
