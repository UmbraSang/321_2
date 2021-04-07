import geocoder
import keyboard  # using module keyboard

#run pip instally geocoder, and pip install keyboard for the program to function as desired

#This chunk of code intends to get the current longitude and latitude of whoever is using the system

#Get location data from geocoder
print("Welcome to Poseidon's CSN geolocation system! Press 'G' on your keyboard to get data on your current location")
g = geocoder.ip('me')

while True:  # making a loop
    try:  # used try so that if user pressed other than the given key error will not be shown
        if keyboard.is_pressed('g'):  # if key is pressed 
            print(f"The country you are in is: {g.country}")
            print(f"The city in which you are accessing this program: {g.address}")
            print(f"Your latitude and longitude coordinates are: {g.latlng}")
            break  # finishing the loop
    except:
        break  # if user pressed a key other than the given key the loop will break
