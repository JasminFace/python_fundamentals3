#EXERCISE 0
fav_colours = ["blue", "red", "maroon", "gray"]
age = [28, 27, 26, 24]
coin_flip = ["tails", "tails", "heads", "heads", "heads"]
fav_artist = ["Simple Plan", "Bruno Mars", "Carly Rae Jepsen"]

words = {
    "cheesy": "Things done or said to make someone feel special",
    "Cloud": "My dog",
    "Kuya": "My brother"
    }

movies = {
    "The Lion King": 1994,
    "Isn't It Romantic": 2019,
    "Deadpool": 2016   
}

cities = {
    "Winnipeg": 749534,
    "Steinbach": 15829,
    "Toronto": 2930000
}

people = {
    "Jasmin": 28,
    "Jeannine": 27,
    "Dylan": 26,
    "Mollin": 24
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

#EXERCISE 3
print(fav_artist[0])
print(fav_artist[1])
for movie, date in movies.items():
    print(f"{movie} was released in {date}.")
age.sort(reverse=True)
print(sorted(age))
movies["Beauty and the Beast"] = 1991, 2017
print(list(movies.items())[-1])

#EXERCISE 4
for num in age: 
    if num > 25: 
        print (num)

age.sort()
print(age[-1])

print(coin_flip.count("heads"))
fav_artist.remove("Carly Rae Jepsen")
cities["Toronto"] = 2930001 

#EXERCISE 5
sum(cities.values())


for person, age in people.items():
    if (age > 27): 
        print(f"{person} is old.")
    else:
        print(f"{person} is young.")

print(fav_colours[-2], fav_colours[-1])

for num in age: 
    print(num + 1)


fav_colours.append("chartreuse")
fav_colours.append("teal")

#EXERCISE 6
more_movies = {
    1999: ["The Matrix", "Star Wars: Episode 1", "The Mummy"]
    2009: ["Avatar", "Star Trek", "District 9"]
    2019: ["How to Train Your Dragon 3", "Toy Story 4", "Star Wars: Episode 9"]
}

phone = [[1,2,3], [4,5,6], [7,8,9,], ["*", 0, "#"]]

countries = [
    {"name": "Canada", "continent": "North America", "island": False}, {"name": "Philippines", "continent": "Asia", "island": True}, {"name": "Paraguay", "continent": "South America", "island": False}
]

#EXERCISE 7
print("I will not skateboard in the halls " * 20)


det = []
def skate ():
    lines = 0
    while lines < 20:
        print("I will not skateboard in the halls")
        lines += 1
        det.append("I will not skateboard in the halls")
skate()


numbers = []
for n in range(1,51):
    print(n)
    numbers.append(n)

sum = 0
for n in numbers:
    sum = sum + n
print(sum)

new_numbers = []
for n in range(1,51):
    print(n)
    print(n)
    print(n)
    new_numbers.append(n)

not_island = []
for island in countries:
    if island["island"] == False:
        not_island.append(island)

print(not_island)

#EXERCISE 8
expenses = [250, 7.95, 30.95, 16.50]
more_expenses = [146.78, 22.22, 99.00, 1]
print(sum(expenses))
print(sum(more_expenses))

#EXERCISE 9
grocery_list = ["carrots", "toilet paper", "apples", "salmon"]

def list():
    for item in grocery_list:
        print(f"*{item}")
    
    if item == "bananas":
        print("You don't need to pick up bananas today")
    else:
        print("You need to pick up bananas")

grocery_list.append("rice")
list()

print(len(grocery_list))

print(grocery_list[1])

grocery_list.sort()
list()

grocery_list.remove("salmon")
list()

#EXERICSE 10
students = {
  'cohort1': 34,
  'cohort2': 42,
  'cohort3': 22
}

def display():
    for key, value in students.items():
        print(f"{key}: {value:.0f} students")
display()

students["cohort4"] = 43
print(students)

print(students.keys())

def expanded():
    for cohort, num in students.items():
        size = num * 1.05
        print(int(size))
expanded()

del students["cohort2"]
print(students)

total = 0
for cohort, num in students.items():
    total += num
print(total)

#EXERCISE 11

range = range(1, 101)
def bitmaker():
    for number in range:
        if number % 3 == 0 and number % 5 == 0:
            print("BitMaker")
        elif number % 3 == 0:
            print("Bit")
        elif number % 5 == 0:
            print("Maker")
        else:
            print(number)

bitmaker()

#EXERCISE 12

def pizzas():
    pizza_num = 0
    print("How many pizzas do you want to order?")
    pizza_quantity = int(input())
    for pizza in range(pizza_quantity):
        pizza_num += 1
        print(f"How many toppings for pizza {pizza_num}?")
        topping_quantity = int(input())
        print(f"You have ordered a pizza with {topping_quantity} toppings")

pizzas()