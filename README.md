# Aktuelles Wetterabruf mit Python

Diese Python-Anwendung ermöglicht es, das aktuelle Wetter für eine bestimmte Stadt abzurufen. Die Wetterdaten werden von der OpenWeatherMap-API bezogen.

## Voraussetzungen

- Python 3.x
- `requests`-Modul: Sie können es mit `pip install requests` installieren.

## Verwendung

1. Erstellen Sie einen API-Schlüssel auf der [OpenWeatherMap-Website](https://home.openweathermap.org/users/sign_up).
2. Fügen Sie den API-Schlüssel in die `get_current_weather`-Funktion im Python-Skript ein.
3. Führen Sie das Python-Skript aus.
4. Das aktuelle Wetter für Braunschweig wird angezeigt. Sie können auch eine andere Stadt angeben, indem Sie den `city`-Parameter der `get_current_weather`-Funktion ändern.

## Beispiel

```python
print(get_current_weather())  # Aktuelles Wetter für Braunschweig
print(get_current_weather("Berlin"))  # Aktuelles Wetter für Berlin
