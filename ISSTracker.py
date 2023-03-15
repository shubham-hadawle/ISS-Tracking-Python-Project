# JSON and urllib.request deal with the data being pulled form the APIs
import json
import urllib.request
# Turle will display the graphics
import turtle
# Webbrowser will open the 'text files' in the Default Text File Application
import webbrowser
# PyAutoGUI will be used to Close the Webbrowser Text File that was open using Webbrowser
import pyautogui
# Geocoder will retrieve our Location based on our IP address
import geocoder
import time

url = 'http://api.open-notify.org/astros.json'
response = urllib.request.urlopen(url)
result = json.loads(response.read())     # A JSON array with current values is loaded into the variable from the API

fp = open("CurrentInfoOfTheISS.txt", "w")
# "number" & "people" are JSON Objects of the JSON Array
fp.writelines("Number of Astronauts currently on board: " + str(result["number"]) + "\n\n")
people = result["people"]
for p in people:
    fp.write(p["name"] + "\n")

# Printing the Latitude & Longitude of the user
g = geocoder.ip('me')
fp.write("\n\nYour current Latitude & Longitudes are: " + str(g.latlng))
fp.close()
webbrowser.open("CurrentInfoOfTheISS.txt")

# Using the Turtle Module to set up the Graphical Part
# Setting up the World Map
screen = turtle.Screen()
screen.setup(1280, 720)
screen.setworldcoordinates(-180, -90, 180, 90)

# Loading the World Map Image
screen.bgpic("world_map_gif.gif")
screen.register_shape("iss_gif.gif")
iss = turtle.Turtle()
iss.shape("iss_gif.gif")
iss.setheading(45)
iss.color("red")
iss.penup()

# Loading the Current Location of the ISS
while True:
    url = 'http://api.open-notify.org/iss-now.json'
    response = urllib.request.urlopen(url)
    result = json.loads(response.read())

    location = result["iss_position"]
    lat = location['latitude']
    long = location['longitude']

    lat = float(lat)
    long = float(long)
    print("\nLatitude: " + str(lat))
    print("\nLongitude: " + str(long))

    iss.goto(long, lat) # Updates the Location of the ISS on the Map
    iss.pendown()
    time.sleep(5) # Refreshes after each 5 seconds

pyautogui.hotkey('ctrl', 'w')
print("Text File containing the Astronauts' Names has been closed.")