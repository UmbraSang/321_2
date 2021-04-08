import geocoder
import keyboard 

#run pip instally geocoder, and pip install keyboard for the program to function as desired

#This chunk of code intends to get the current longitude and latitude of whoever is using the system


print("Welcome to Poseidon's CSN geolocation system! Press 'G' on your keyboard to get data on your current location")
#Get location data from geocoder
g = geocoder.ip('me')

#Test that the location data returns data for our current location (Victoria, Canada)
def locationtester(location):
    testBoolean = True
    if (location.country!="CA"):
        testBoolean = False
    
    if(location.address!="Victoria, British Columbia, CA"):
       testBoolean = False 
    
    if(location.latlng== None):
        testBoolean = False
    return testBoolean

    

while True:  
    try:  
        if keyboard.is_pressed('g'):  # if key is pressed 
            #location data will only print if user's location is in Victoria
            if(locationtester(g)):
                print(f"\nThe country you are in is: {g.country}")
                print(f"The city in which you are accessing this program: {g.address}")
                print(f"Your latitude and longitude coordinates are: {g.latlng}")
            break  
    except:
        break




