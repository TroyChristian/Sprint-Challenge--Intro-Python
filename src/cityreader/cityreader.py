
#  Create a class to hold a city location. Call the class "City". It should have
# fields for name, lat and lon (representing latitude and longitude).


# We have a collection of US cities with population over 750,000 stored in the
# file "cities.csv". (CSV stands for "comma-separated values".)
#
# In the body of the `cityreader` function, use Python's built-in "csv" module 
# to read this file so that each record is imported into a City instance. Then
# return the list with all the City instances from the function.
# Google "python 3 csv" for references and use your Google-fu for other examples.
#
# Store the instances in the "cities" list, below.
#
# Note that the first line of the CSV is header that describes the fields--this
# should not be loaded into a City object.
###MY NOTES:
# city,state_name,county_name,lat,lng,population,density,timezone,zips
# Seattle,Washington,King,47.6217,-122.3238,3541236,3243,America/Los_Angeles,98109 98108 98104 98107 98106 98101 98103 98102 98105 98154 98122 98121 98126 98125 98178 98174 98177 98144 98146 98195 98199 98118 98119 98116 98117 98115 98112 98164 98134 98136 98133 98111 98113 98114 98124 98127 98129 98139 98141 98145 98161 98165 98170 98175 98181 98185 98191 98194

# Open CSV file
path = "/Users/lambda_school_loaner_219/Documents/Python/Sprint-Challenge--Intro-Python/src/cities.csv"




class City():
 def __init__(self, name, lat, lon):
  self.name = name 
  self.lat = lat
  self.lon = lon 


cities = []

def cityreader(cities=[]):
  # TODO Implement the functionality to read from the 'cities.csv' file
  # For each city record, create a new City instance and add it to the 
  # `cities` list
    
    return cities

cityreader(cities)

# Print the list of cities (name, lat, lon), 1 record per line.
for c in cities:
    print(c)

# STRETCH GOAL!
#
# Allow the user to input two points, each specified by latitude and longitude.
# These points form the corners of a lat/lon square. Pass these latitude and 
# longitude values as parameters to the `cityreader_stretch` function, along
# with the `cities` list that holds all the City instances from the `cityreader`
# function. This function should output all the cities that fall within the 
# coordinate square.
#
# Be aware that the user could specify either a lower-left/upper-right pair of
# coordinates, or an upper-left/lower-right pair of coordinates. Hint: normalize
# the input data so that it's always one or the other, then search for cities.
# In the example below, inputting 32, -120 first and then 45, -100 should not
# change the results of what the `cityreader_stretch` function returns.
#
# Example I/O:
#
# Enter lat1,lon1: 45,-100
# Enter lat2,lon2: 32,-120
# Albuquerque: (35.1055,-106.6476)
# Riverside: (33.9382,-117.3949)
# San Diego: (32.8312,-117.1225)
# Los Angeles: (34.114,-118.4068)
# Las Vegas: (36.2288,-115.2603)
# Denver: (39.7621,-104.8759)
# Phoenix: (33.5722,-112.0891)
# Tucson: (32.1558,-110.8777)
# Salt Lake City: (40.7774,-111.9301)

# TODO Get latitude and longitude values from the user

def cityreader_stretch(lat1, lon1, lat2, lon2, cities=[]):
  # within will hold the cities that fall within the specified region
  within = []

  # TODO Ensure that the lat and lon valuse are all floats
  # Go through each city and check to see if it falls within 
  # the specified coordinates.

  return within
