import tkinter as tk
from tkinter import messagebox

from weather import get_weather


# Function to get weather information
def show_weather():
    city = city_entry.get().strip()

    # Check whether city name is entered
    if city == "":
        messagebox.showwarning(
            "Input Error",
            "Please enter a city name."
        )
        return

    try:
        # Get weather data
        weather = get_weather(city)

        # Display information
        city_label.config(
            text=f"City: {weather['city']}"
        )

        country_label.config(
            text=f"Country: {weather['country']}"
        )

        temperature_label.config(
            text=f"Temperature: {weather['temperature']} °C"
        )

        feels_like_label.config(
            text=f"Feels Like: {weather['feels_like']} °C"
        )

        condition_label.config(
            text=f"Condition: {weather['condition'].title()}"
        )

        humidity_label.config(
            text=f"Humidity: {weather['humidity']}%"
        )

        wind_label.config(
            text=f"Wind Speed: {weather['wind_speed']} m/s"
        )

        pressure_label.config(
            text=f"Pressure: {weather['pressure']} hPa"
        )

        visibility_label.config(
            text=f"Visibility: {weather['visibility']:.1f} km"
        )

    except Exception as error:
        messagebox.showerror(
            "Error",
            str(error)
        )


# Function to clear information
def clear_weather():
    city_entry.delete(0, tk.END)

    city_label.config(text="City:")
    country_label.config(text="Country:")
    temperature_label.config(text="Temperature:")
    feels_like_label.config(text="Feels Like:")
    condition_label.config(text="Condition:")
    humidity_label.config(text="Humidity:")
    wind_label.config(text="Wind Speed:")
    pressure_label.config(text="Pressure:")
    visibility_label.config(text="Visibility:")


# Create main window
root = tk.Tk()

root.title("Weather Information System")
root.geometry("550x650")
root.resizable(False, False)
root.configure(bg="#EAF4FF")


# Title
title_label = tk.Label(
    root,
    text="Weather Information System",
    font=("Arial", 24, "bold"),
    bg="#EAF4FF",
    fg="#1E3A5F"
)

title_label.pack(pady=25)


# City input label
input_label = tk.Label(
    root,
    text="Enter City Name:",
    font=("Arial", 14),
    bg="#EAF4FF"
)

input_label.pack()


# City input box
city_entry = tk.Entry(
    root,
    font=("Arial", 14),
    width=30,
    justify="center"
)

city_entry.pack(pady=10)


# Buttons frame
button_frame = tk.Frame(
    root,
    bg="#EAF4FF"
)

button_frame.pack(pady=10)


# Get Weather button
get_button = tk.Button(
    button_frame,
    text="Get Weather",
    font=("Arial", 12, "bold"),
    command=show_weather,
    width=12,
    bg="#4CAF50",
    fg="white"
)

get_button.grid(row=0, column=0, padx=5)


# Clear button
clear_button = tk.Button(
    button_frame,
    text="Clear",
    font=("Arial", 12, "bold"),
    command=clear_weather,
    width=10,
    bg="#FFA500",
    fg="white"
)

clear_button.grid(row=0, column=1, padx=5)


# Exit button
exit_button = tk.Button(
    button_frame,
    text="Exit",
    font=("Arial", 12, "bold"),
    command=root.destroy,
    width=10,
    bg="#F44336",
    fg="white"
)

exit_button.grid(row=0, column=2, padx=5)


# Weather information frame
weather_frame = tk.Frame(
    root,
    bg="white",
    bd=2,
    relief="groove"
)

weather_frame.pack(
    padx=30,
    pady=25,
    fill="both"
)


# Weather information labels
city_label = tk.Label(
    weather_frame,
    text="City:",
    font=("Arial", 14),
    bg="white",
    anchor="w"
)

city_label.pack(
    padx=20,
    pady=7,
    anchor="w"
)


country_label = tk.Label(
    weather_frame,
    text="Country:",
    font=("Arial", 14),
    bg="white",
    anchor="w"
)

country_label.pack(
    padx=20,
    pady=7,
    anchor="w"
)


temperature_label = tk.Label(
    weather_frame,
    text="Temperature:",
    font=("Arial", 14),
    bg="white",
    anchor="w"
)

temperature_label.pack(
    padx=20,
    pady=7,
    anchor="w"
)


feels_like_label = tk.Label(
    weather_frame,
    text="Feels Like:",
    font=("Arial", 14),
    bg="white",
    anchor="w"
)

feels_like_label.pack(
    padx=20,
    pady=7,
    anchor="w"
)


condition_label = tk.Label(
    weather_frame,
    text="Condition:",
    font=("Arial", 14),
    bg="white",
    anchor="w"
)

condition_label.pack(
    padx=20,
    pady=7,
    anchor="w"
)


humidity_label = tk.Label(
    weather_frame,
    text="Humidity:",
    font=("Arial", 14),
    bg="white",
    anchor="w"
)

humidity_label.pack(
    padx=20,
    pady=7,
    anchor="w"
)


wind_label = tk.Label(
    weather_frame,
    text="Wind Speed:",
    font=("Arial", 14),
    bg="white",
    anchor="w"
)

wind_label.pack(
    padx=20,
    pady=7,
    anchor="w"
)


pressure_label = tk.Label(
    weather_frame,
    text="Pressure:",
    font=("Arial", 14),
    bg="white",
    anchor="w"
)

pressure_label.pack(
    padx=20,
    pady=7,
    anchor="w"
)


visibility_label = tk.Label(
    weather_frame,
    text="Visibility:",
    font=("Arial", 14),
    bg="white",
    anchor="w"
)

visibility_label.pack(
    padx=20,
    pady=7,
    anchor="w"
)


# Start the application
root.mainloop()