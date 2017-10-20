names = ['Frank', 'Dee', 'Charlie', 'Mac', 'Dennis']
for n in names:
    print('Hey-lo ' + n)

names[0] = 'Pondee'

names.append('Frank')

for n in names:
    print('Hi-lo ' + n)

blah = names.pop()

print(blah)