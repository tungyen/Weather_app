import tkinter as tk
from tkinter import ttk
import requests
from PIL import Image, ImageTk
from datetime import datetime

# My api for openWeather API
api_key = "774f3f8413fcfcbe6578124660cf3b3c"

global showInfoPM

def getData(city):
    url = 'http://api.openweathermap.org/data/2.5/weather?q={}&appid={}&units=metric'.format(city, api_key)
    response = requests.get(url)
    data = response.json()
    return data

# Call the openWeather API to get the information of the city weather
def fetchWeather(city):
    data = getData(city)
    humidity = data['main']['humidity']
    pressure = data['main']['pressure']
    wind = data['wind']['speed']
    description = data['weather'][0]['description']
    temp = data['main']['temp']
    tempLabel.config(text=f"Temperature of {city}: {temp} Celsius")
    humidityLabel.config(text=f"Humidity of {city}: {humidity}%")
    windLabel.config(text=f"Wind speed of {city}: {wind}m/s")
    disLabel.config(text=f"Weather description of {city}: {description}")
    pressureLabel.config(text=f"Atmosphere of {city}: {pressure} pa")
    
def getUserLoc():
    response = requests.get('http://ipinfo.io/json')
    data = response.json()
    city = data.get('city')
    region = data.get('region')
    country = data.get('country')
    fetchWeather(city)
    
def showPM():
    global showInfoPM
    if showInfoPM:
        pmLabel.config(text="The Product Manager Accelerator Program is designed to support PM professionals through every stage of their career. From students looking for entry-level jobs to Directors looking to take on a leadership role, our program has helped over hundreds of students fulfill their career aspirations.")
    else:
        pmLabel.config(text="")
    showInfoPM = not showInfoPM


# Create the main window
showInfoPM = False
root = tk.Tk()
root.title("Weather App")
root.geometry("800x600")  # Set window size

# Label and entry for city name
NameInfo = tk.Label(root, text="Welcome to Corey Chiang's Weather API")
NameInfo.pack(pady=10)
city_label = tk.Label(root, text="Enter City:")
city_label.pack(pady=10)
city_entry = tk.Entry(root, width=25)
city_entry.pack()

# Button to fetch weather
fetch_button = tk.Button(root, text="Get Weather", command=lambda: fetchWeather(city_entry.get()))
fetch_button.pack(pady=10)
locate_button = tk.Button(root, text="Local Weather", command=lambda: getUserLoc())
locate_button.pack(pady=10)
PM_info_button = tk.Button(root, text="Check information of PM Accelerator", command=lambda: showPM())
PM_info_button.pack(pady=10)

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
pmLabel = tk.Label(weather_frame, text="Info of PM Accelerator")
pmLabel.grid(row=5, column=0, sticky="w")
root.mainloop()

