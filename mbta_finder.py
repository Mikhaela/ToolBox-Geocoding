"""
Geocoding and Web APIs Project Toolbox exercise

Find the MBTA stops closest to a given location.

Full instructions are at:
https://sites.google.com/site/sd15spring/home/project-toolbox/geocoding-and-web-apis
"""

import urllib   # urlencode function
import urllib2  # urlopen function (better than urllib version)
import json
from pprint import pprint 


# Useful URLs (you need to add the appropriate parameters for your requests)
GMAPS_BASE_URL = "https://maps.googleapis.com/maps/api/geocode/json"
MBTA_BASE_URL = "http://realtime.mbta.com/developer/api/v2/stopsbylocation"
MBTA_DEMO_API_KEY = "wX9NwuHnZU2ToO7GmGR9uw"

# url = "https://maps.googleapis.com/maps/api/geocode/json?address=Fenway%20Park" 
# f = urllib2.urlopen(url)
# response_text = f.read()
# response_data = json.loads(response_text)
# pprint(response_data)
# print response_data["results"][0]["geometry"]
# A little bit of scaffolding if you want to use it

def get_json(url):
    """
    Given a properly formatted URL for a JSON web API request, return
    a Python JSON object containing the response to that request.
    """ 
    f = urllib2.urlopen(url)
    response_text = f.read()
    response_data = json.loads(response_text)

    return response_data


def get_lat_long(place_name):
    """
    Given a place name or address, return a (latitude, longitude) tuple
    with the coordinates of the given place.

    See https://developers.google.com/maps/documentation/geocoding/
    for Google Maps Geocode API URL formatting requirements.
    """
    dictionary = { 'address' : place_name }
    start = "https://maps.googleapis.com/maps/api/geocode/json?" 
    end = urllib.urlencode(dictionary)
    url = start + end 

    response_data = get_json(url)

    lat_lng = response_data["results"][0]["geometry"]["location"]
    lat = lat_lng['lat']
    lng = lat_lng['lng']

    return lat,lng

def get_nearest_station(latitude, longitude):
    """
    Given latitude and longitude strings, return a (station_name, distance)
    tuple for the nearest MBTA station to the given coordinates.

    See http://realtime.mbta.com/Portal/Home/Documents for URL
    formatting requirements for the 'stopsbylocation' API.
    """
    dictionary = {'format':'json' , 'lat':latitude , 'lon':longitude} 
    start = 'http://realtime.mbta.com/developer/api/v2/stopsbylocation?api_key=wX9NwuHnZU2ToO7GmGR9uw&'
    end = urllib.urlencode(dictionary)
    url = start + end 

    response_data = get_json(url) 

    stop_name = response_data["stop"][0]["stop_name"]
    distance =  response_data["stop"][0]["distance"]
    return '{} is {} miles away'.format(stop_name,distance)


somewhere = "Dwelltime Cambridge MA"
print get_nearest_station(get_lat_long(somewhere)[0],get_lat_long(somewhere)[1])

