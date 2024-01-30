from numpy import place
import requests
import pandas as pd
import googlemaps
from datetime import datetime
import pandas as pd

class googleMapsClient():
    def __init__(self):
        self.url = 'https://routes.googleapis.com/directions/v2:computeRoutes'
        self.key = 'API_KEY'
        self.gmaps = googlemaps.Client(key=self.key)
    def queryAutocomplete(self, query):
        queryAutocomplete = requests.get(url=f'https://maps.googleapis.com/maps/api/place/queryautocomplete/json?input={query}&key={self.key}')
        self.places = pd.DataFrame(queryAutocomplete.json()['predictions']).values.tolist()
        return self.places
    def getPlaceDetails(self, placeIndex):
        fields = [
            'business_status',
            'formatted_address',
            'name',
            'formatted_phone_number',
            'opening_hours',
            'rating',
            'url',
        ]
        if type(self.places[placeIndex][4]) == float:
            return "Invalid option. Please choose another location"

        else:
            placeDetail = requests.get(url=f'https://maps.googleapis.com/maps/api/place/details/json?place_id={self.places[placeIndex][4]}&fields={",".join(fields)}&key={self.key}')
            if 'error_message' in placeDetail.json():
                return "Invalid option. Please choose another location"
            else:
                placeDetail = placeDetail.json()['result']
            
                businessStatus = f"Business Status: {placeDetail['business_status']} \n",
                formattedAddress = f"Address: {placeDetail['formatted_address']} \n",
                name = f"Name: {placeDetail['name']} \n",
                phoneNumber = f"Phone Number: {placeDetail['formatted_phone_number']} \n",
                openingHours = f"Opening Now: {placeDetail['opening_hours']['open_now']} \n",
                rating = f"Rating: {placeDetail['rating']} \n",
                mapsUrl = f"Maps Url: {placeDetail['url']} \n",
                return businessStatus, formattedAddress, name, phoneNumber, openingHours, rating, mapsUrl 
