"""Time to play with Python dictionaries!
You're going to work on a dictionary that
stores cities by country and continent.
One is done for you - the city of Mountain 
View is in the USA, which is in North America.

You need to add the cities listed below by
modifying the structure.
Then, you should print out the values specified
by looking them up in the structure.

Cities to add:
Bangalore (India, Asia)
Atlanta (USA, North America)
Cairo (Egypt, Africa)
Shanghai (China, Asia)"""

#from collections import defaultdict

#locations = {'North America': {'USA': ['Mountain View']}}

"""Print the following (using "print").
1. A list of all cities in the USA in
alphabetic order.
2. All cities in Asia, in alphabetic
order, next to the name of the country.
In your output, label each answer with a number
so it looks like this:
1
American City
American City
2
Asian City - Country
Asian City - Country"""

#Solution

#Practices to add items to the dict using a class

class Cities:
    def __init__(self):
        self.data = {}
    
    def add(self,continent,country,city):
        country_set = self.data.setdefault(continent,{})
        city_list = country_set.setdefault(country,[])
        city_list.append(city)   

locations = Cities()
locations.add('North America','USA','Mountain View')

locations.add('Asia','India','Bangalore')
locations.add('North America','USA','Atlanta')
locations.add('Africa','Egypt','Cairo')
locations.add('Asia','China','Shanghai')


print("1")
am_cities = locations.data.get('North America').get('USA')
am_cities.sort()
print(*(c for c in am_cities), sep='\n')

print("2")
asia_list = []
asia_countries = locations.data.get('Asia')
for country in asia_countries:
    cities = asia_countries.get(country)
    for city in cities:
        asia_list.append(f"{city} - {country}")
        
asia_list.sort()
print(*(c for c in asia_list), sep='\n')



