names = ['Frank', 'Dee', 'Charlie', 'Mac', 'Dennis']
for n in names:
    print('Hey-lo ' + n)

names[0] = 'Pondee'

names.append('Frank')

for n in names:
    print('Hi-lo ' + n)

blah = names.pop(0)

print(blah)

for n in names:
    print('Hey-O ' + n)

names.remove('Dennis')

print(names)
