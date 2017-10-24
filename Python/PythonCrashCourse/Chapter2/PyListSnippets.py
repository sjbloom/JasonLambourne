#######################################################################################################
# Soring lists
#######################################################################################################
spots = ['Rucker Park', 'EMB', 'The BIG House', 'Stamford Bridge']
print(spots)
print(sorted(spots))
print(spots)
print(sorted(spots, reverse=True))
spots.reverse()
print(spots)
spots.sort(reverse=True)
#######################################################################################################
# pop function removes items from a list
#######################################################################################################
generic_list = ['a', 'b', 'c', 'd']
print('pre pop')
print(generic_list)
generic_list.pop()
print('post pop')
print(generic_list)
#######################################################################################################
# loop thru a list
#######################################################################################################
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician.title() + " that trick was off the chaizzle")
    print("Bust another one, " + magician.title() + '\n')

print('Yeah yeah, that\'s it for tonight, yall')
#######################################################################################################
# Other useful list stuff
#######################################################################################################
# - create a numerical list using the range function
numbers = list(range(1, 6))
print(numbers)
# - even numbers list
even_numbers = list(range(2, 11, 2))
print(even_numbers)
# - list of squares
squares = []
for value in range(1, 11):
    squares.append(value**2)
print(squares)
# - simple descriptive stat functions with lists of numbers
digits = list(range(0, 11))
print(min(digits))
print(max(digits))
print(sum(digits))
# -build the squares list using a list comprehension
squares = [value**2 for value in range(1, 11)]
print(squares)
#######################################################################################################
# -slices
#######################################################################################################
players = ['John', 'Karl', 'Jeff', 'Antoine', 'Greg']
print(players[0:2])  # first two players
print(players[:3])   # will start at the beginning
print(players[2:])   # will return all list items starting @ 3
print(players[-2:])  # last two players
# - Loop through a slice
i = 1
print('Here are the first three players on the team: ')
for player in players[:3]:
    print(str(i) + '. ' + player.title())
    i += 1
# - Copy an entire list using slice syntax
original_team = players[:]
print(original_team)
# if this was done "original_team = players" it doesn't copy the list it points them to the same thing.
