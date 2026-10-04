# Weather Information System Using Python

## 1. Project Title

**Weather Information System Using Python**

## 2. Introduction

The Weather Information System is a Python-based desktop application developed using Tkinter. It allows users to enter a city name and obtain current weather information through the OpenWeatherMap API.

The application displays important weather details such as temperature, humidity, wind speed, pressure, visibility, and weather condition.

## 3. Problem Statement

Checking weather information manually from different websites or applications can be inconvenient. This project provides a simple desktop application where users can enter a city name and receive current weather information in one place.

## 4. Objectives

* To develop a simple weather application using Python.
* To create a graphical user interface using Tkinter.
* To connect Python with a weather API.
* To process JSON data received from the API.
* To display current weather information.
* To handle invalid input and network errors.

## 5. Technologies Used

* Python
* Tkinter
* Requests
* JSON
* OpenWeatherMap API
* VS Code

## 6. System Requirements

### Hardware

* Computer/Laptop
* Internet connection
* Minimum 4 GB RAM

### Software

* Windows/Linux/macOS
* Python 3.x
* VS Code or another Python IDE
* Requests library

## 7. Working Methodology

The user enters the name of a city in the input box.

The application sends a request to the OpenWeatherMap API.

The API returns weather information in JSON format.

Python processes the JSON data and extracts the required values.

The extracted information is displayed in the Tkinter GUI.

## 8. System Flow

```text
User enters city
       ↓
Click Get Weather
       ↓
Python sends API request
       ↓
OpenWeatherMap API
       ↓
JSON response
       ↓
Python processes data
       ↓
Weather information displayed
```

## 9. Modules

### Module 1: User Interface

Tkinter is used to create the graphical interface.

### Module 2: API Request

The Requests library sends an HTTP request to the weather API.

### Module 3: JSON Processing

The API response is received as JSON and converted into a Python dictionary.

### Module 4: Weather Display

The application displays temperature, humidity, wind speed, pressure, visibility, and weather condition.

### Module 5: Error Handling

The application handles invalid cities, network problems, invalid API keys, and request timeouts.

## 10. Python Concepts Used

* Variables
* Functions
* Dictionaries
* Conditional statements
* Exception handling
* Modules
* JSON
* API requests
* Tkinter
* String formatting

## 11. Sample Output

```text
Weather Information System

Enter City Name:
[ New Delhi ]

City: New Delhi
Country: IN
Temperature: 28 °C
Feels Like: 30 °C
Condition: Clear Sky
Humidity: 45%
Wind Speed: 3.5 m/s
Pressure: 1012 hPa
Visibility: 10 km
```

The actual values depend on the current weather returned by the API.

## 12. Advantages

* Simple and easy to use.
* Provides current weather information.
* User-friendly graphical interface.
* Reduces the need for manual searching.
* Demonstrates real-world API integration.

## 13. Limitations

* Requires an internet connection.
* Requires a valid API key.
* Weather information depends on the API.
* The application provides current information rather than long-term weather analysis.

## 14. Future Scope

The project can be improved by adding:

* Five-day weather forecast.
* Weather icons.
* Sunrise and sunset times.
* Automatic location detection.
* Multiple-city comparison.
* Temperature charts.
* Dark mode.
* Better graphical design.
* Database support for storing searched cities.

## 15. Conclusion

The Weather Information System demonstrates how Python can be used to create a practical desktop application. Tkinter provides the graphical interface, while the Requests library connects the application to the weather API. JSON data received from the API is processed and displayed to the user.

This project helps demonstrate Python programming, GUI development, API integration, JSON processing, and exception handling.

## 16. API Key Configuration

The API key should be stored in `weather.py`.

```python
API_KEY = "YOUR_API_KEY"
```

Replace `YOUR_API_KEY` with your own API key.

Do not publish or share the real API key.
