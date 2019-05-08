fav_colours = ["blue", "red", "maroon", "gray"]
age = [28, 27, 26, 24]
coin_flip = ["tails", "tails", "heads", "heads", "heads"]
fav_artist = ["Simple Plan", "Bruno Mars", "Carly Rae Jepsen"]

words = {
    "cheesy": "Things done or said to make someone feel special",
    "Cloud": "My dog",
    "Kuya": "My brother",
    }

movies = {
    "The Lion King": 1994,
    "Isn't It Romantic": 2019,
    "Deadpool": 2016,    
}

cities = {
    "Winnipeg": 749534,
    "Steinbach": 15829,
    "Toronto": 2930000,
}

people = {
    "Jasmin": 28,
    "Jeannine": 27,
    "Dylan": 26,
    "Mollin": 24,
    }

#EXERCISE 1
print(coin_flip)
print(fav_colours[0])
print(sorted(age))
age.append(0)
print(movies.get("The Lion King"))

#EXERCISE 2
print(fav_colours[-1])
cities["Los Angeles"] = 4000000
coin_flip.sort(reverse=True)
print(cities.get("Steinbach"))
for artist in fav_artist:
    print(f"{artist} is DA BOMB!")
