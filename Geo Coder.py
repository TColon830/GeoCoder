import requests
import json

#Short program to pull X and Y cooridnates from NYC Geoclient for mapping purposes

def xy_by_address(houseNum, street, borough):
	#These values are generated by NYC geocoder, to create an API account, go to:
	#https://api.cityofnewyork.us/geoclient/v1/doc
	#Once you have a user name and password, create a new project and generate an app_key and 
	#app_password
	app_key = 'REMOVED'
	auth_key = 'REMOVED'
	call = 'https://api.cityofnewyork.us/geoclient/v1/address.json?houseNumber={}&street={}&borough={}&app_id={}&app_key={}'.format(houseNum, street, borough, app_key,auth_key)

	try:
		#Send our call to the server:
		response = requests.get(call)

		if response.status_code == 200:
		    data = response.json()
		    return data['address']['xCoordinate'], data['address']['yCoordinate']
		else:
		    print('Failed to get map data, response code:' + str(response.status_code))

	except:
		ValueError("Unknown location")

def xy_by_intersection(crossStreet1, crossStreet2, borough):
	app_key = 'REMOVED'
	auth_key = 'REMOVED'
	call = 'https://api.cityofnewyork.us/geoclient/v1/intersection.json?crossStreetOne={}&crossStreetTwo={}&borough={}&app_id={}&app_key={}'.format(crossStreet1, crossStreet2, borough, app_key,auth_key)

	try:
		#Send our call to the server:
		response = requests.get(call)

		if response.status_code == 200:
		    data = response.json()
		    return data['intersection']['xCoordinate'], data['intersection']['yCoordinate']
		else:
		    print('Failed to get map data, response code:' + str(response.status_code))

	except:
		ValueError("Unknown location")

# print('Test by address: ', xy_by_address('120-55','queens blvd', 'Queens'))
# print('Test by cross streets: ', xy_by_intersection('Amboy Road','Pleasant Plains Avenue', 'Staten Island'))
# print('Test by address: ', xy_by_address('120-55','okwdokwd street', 'Queens'))