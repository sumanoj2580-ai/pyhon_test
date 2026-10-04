import requests

# Put your OpenWeatherMap API key here
API_KEY = "13f73f20351261f82c38e22b9e9cd445"

BASE_URL = "https://api.openweathermap.org/data/2.5/weather"


def get_weather(city):
    """
    Fetch weather information for the given city.
    """

    params = {
        "q": city,
        "appid": API_KEY,
        "units": "metric"
    }

    try:
        response = requests.get(BASE_URL, params=params, timeout=10)

        # Check if API request was successful
        if response.status_code == 200:

            # Convert JSON response into Python dictionary
            data = response.json()

            weather_data = {
                "city": data["name"],
                "country": data["sys"]["country"],
                "temperature": data["main"]["temp"],
                "feels_like": data["main"]["feels_like"],
                "condition": data["weather"][0]["description"],
                "humidity": data["main"]["humidity"],
                "wind_speed": data["wind"]["speed"],
                "pressure": data["main"]["pressure"],
                "visibility": data.get("visibility", 0) / 1000
            }

            return weather_data

        elif response.status_code == 404:
            raise Exception("City not found. Please enter a valid city name.")

        elif response.status_code == 401:
            raise Exception("Invalid API key.")

        else:
            raise Exception("Unable to fetch weather information.")

    except requests.exceptions.ConnectionError:
        raise Exception("No internet connection.")

    except requests.exceptions.Timeout:
        raise Exception("Request timed out. Please try again.")

    except requests.exceptions.RequestException:
        raise Exception("Network error occurred.")