import geocoder

#This chunk of code intends to get the current longitude and latitude of whoever is using the system

#Get location data from geocoder
g = geocoder.ip('me')


print(f"The country you are in is: {g.country}")
print(f"The city you reside in is: {g.address}")
print(f"Your latitude and longitude coordinates are: {g.latlng}")

