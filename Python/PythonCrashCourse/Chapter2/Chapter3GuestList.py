# Exercises 3.4 - 3.7
def inviteGuestList(listToPrint):
    for guest in listToPrint:
        print('Yo ' + guest + ' down to grab some food?')


# define guest list
guestList = ['Bob Marley', 'Big Pun', 'John Lennon']
# extend invitation to guests
inviteGuestList(guestList)
# remove a guest
looser = guestList.pop(-1)
print('\nLooks like ' + looser + ' doesn\'t eat food, so no dice there.\n')
# add a new guest
guestList.append('Jimmy Hendrix')
inviteGuestList(guestList)
# add more people to the guest list
guestList.insert(3, 'Rah Digga')
guestList.insert(3, 'Arianna Grande')
guestList.append('Slick Rick')
inviteGuestList(guestList)
# delete all but 2 guests
print('\nOH SNAP! I can only eat with two of you...sorry\n')

while (len(guestList) > 2):
    poppedGuest = guestList.pop(-1)
    print('We\'ll have to link up some other time, ' + poppedGuest)

# invite the final 2 guests
print('\n')
inviteGuestList(guestList)

# cancel and remove the last two guests
while (len(guestList) > 0):
    print('never mind ' + guestList[0] + '...too much work...later')
    del guestList[0]

print(guestList)
