# variables
new_xpos = 5
x = 6
new_xpos += 5
print(new_xpos+x)

tupla = (100,200)

new_tupla = tupla + (300,)
del new_tupla
len(tupla)
min(tupla)
max(tupla)

contains = 100 in tupla

print(tupla)
print(contains)

movement = [-1,0,1,2,3]
movement[0] = -2
movement.append(4)
movement.remove(3)
print(movement[0])
print(movement)

start_posi = {'p1': 50, 'p2': 100, 'p3': 150}


start_posi['p1']
start_posi.keys()