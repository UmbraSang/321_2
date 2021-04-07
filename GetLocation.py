import geocoder
import keyboard  # using module keyboard

#run pip instally geocoder, and pip install keyboard for the program to function as desired

#This chunk of code intends to get the current longitude and latitude of whoever is using the system


print("Welcome to Poseidon's CSN geolocation system! Press 'G' on your keyboard to get data on your current location")
#Get location data from geocoder
g = geocoder.ip('me')

while True:  
    try:  
        if keyboard.is_pressed('g'):  # if key is pressed 
            print(f"The country you are in is: {g.country}")
            print(f"The city in which you are accessing this program: {g.address}")
            print(f"Your latitude and longitude coordinates are: {g.latlng}")
            break  
    except:
        break  
