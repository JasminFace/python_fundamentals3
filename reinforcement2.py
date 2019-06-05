schedule = [
{'train': "72C", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "72D", 'frequency_in_minutes': 15, 'direction': "south"},
{'train': "610", 'frequency_in_minutes': 5, 'direction': "north"},
{'train': "611", 'frequency_in_minutes': 5, 'direction': "south"},
{'train': "80A", 'frequency_in_minutes': 30, 'direction': "east"},
{'train': "80B", 'frequency_in_minutes': 30, 'direction': "west"},
{'train': "110", 'frequency_in_minutes': 15, 'direction': "north"},
{'train': "111", 'frequency_in_minutes': 15, 'direction': "south"}
]

# train111_direction = schedule[7]['direction']
# print(train111_direction)

# train80B_freq = schedule[6]['frequency_in_minutes']
# print(train80B_freq)

# train610_direction = schedule[2]['direction']
# print(train610_direction)

# north_trains = []
# for train in schedule:
#     if train['direction'] == 'north':
#         north_trains.append(train)
# print(north_trains)

# east_trains = []
# for train in schedule:
#     if train['direction'] == 'east':
#         east_trains.append(train)
# print(east_trains)

# def train_direction(direction):
#     for train in schedule:
#         if train['direction'] == direction:
#             print(train)

# train_direction('north')
# train_direction('east')

# train = schedule[5]
# train['first_departure_time'] = 8
# print(train)

trains_by_frequency = {}
for train in schedule:
    freq = train['frequency_in_minutes']
    name = train['train']
    if freq in trains_by_frequency:
        trains_by_frequency[freq].append(name)
    else:
        trains_by_frequency[freq] = [name]
print(trains_by_frequency)
