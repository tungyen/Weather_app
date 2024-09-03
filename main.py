import tkinter as tk
from tkinter import ttk
import requests

api_key = "774f3f8413fcfcbe6578124660cf3b3c"

def fetch_weather(city):
    # Placeholder for weather fetching logic
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, api_key)
    response = requests.get(url)
    data = response.json()
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    print(data)
    tempLabel.config(text=f"Temperature of {city}: {temp} Celsius")
    humidityLabel.config(text=f"Humidity of {city}: {humidity}%")
    windLabel.config(text=f"Wind speed of {city}: {wind}m/s")
    disLabel.config(text=f"Weather description of {city}: {description}")
    pressureLabel.config(text=f"Atmosphere of {city}: {pressure} pa")
    

# Create the main window
root = tk.Tk()
root.title("Weather App")
root.geometry("800x600")  # Set window size

# Label and entry for city name
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)
city_entry = tk.Entry(root, width=25)
city_entry.pack()

# Button to fetch weather
fetch_button = tk.Button(root, text="Get Weather", command=lambda: fetch_weather(city_entry.get()))
fetch_button.pack(pady=10)

weather_frame = tk.Frame(root)
weather_frame.pack(pady=10)

# Label to display the weather information
tempLabel = tk.Label(weather_frame, text="Temperature: ")
tempLabel.grid(row=0, column=0, sticky="w")
humidityLabel = tk.Label(weather_frame, text="Humidity: ")
humidityLabel.grid(row=1, column=0, sticky="w")
windLabel = tk.Label(weather_frame, text="Wind Speed: ")
windLabel.grid(row=2, column=0, sticky="w")
disLabel = tk.Label(weather_frame, text="Weather Description: ")
disLabel.grid(row=3, column=0, sticky="w")
pressureLabel = tk.Label(weather_frame, text="Atmosphere Pressure: ")
pressureLabel.grid(row=4, column=0, sticky="w")
root.mainloop()

