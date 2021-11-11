#create a mapping of state to abbreviation
states = {
    'oregin':'or',
    'florida':'fl',
    'california':'ca',
    'new york':'ny',
    'michigan':'mi'
}

#create a basic set of states and some cities in them
cities = {
    'ca':'san francisco',
    'mi':'detroit',
    'fl':'jacksonville'
}

#add some more cities
cities['ny'] = 'new york'
cities['or'] = 'portland'

#print out some cities
print('-'*10)
print("ny state has: ",cities['ny'])
print("or state has: ",cities['or'])

#print some states
print('-'*10)
print("michigan's abbreviation is: ",states['michigan'] )
print("florida's abbreviation is: ",states['florida'] )

#do it by using the state then cities dict
print('-'*10)
print("michigan's abbreviation is: ",cities[states['michigan']] )
print("florida's abbreviation is: ",cities[states['florida']] )

#print every state abbreviation
print('-'*10)
for state,abbrev in list(states.items()):
    print(f"{state} is abbreviated {abbrev}")

#print every city in state
print('-'*10)
for abbrev,city in list(cities.items()):
    print(f"{abbrev} has the city {city}")

#now fo both at the same time
print('-'*10)
for state,abbrev in list(states.items()):
    print(f"{state} state is abbreviated {abbrev}")
    print(f"and has city {cities[abbrev]}")

print('-'*10)
#~~~~
#~~~~

if not state:
    print("sorry,no texas.")

#ssssssssssssss
city = cities.get('tx','does not exist')
print(f"the city for the state 'tx' is :{city}")
