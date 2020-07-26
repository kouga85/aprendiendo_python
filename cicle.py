"""
#ciclo IF
is_game_over = False
is_heroe_x_pos = 0
is_enemie_x_pos = 3
is_enemie_x_pos1 = 5

is_heroe_x_pos += 3
if is_heroe_x_pos == is_enemie_x_pos:
    is_game_over = True
elif is_heroe_x_pos == is_enemie_x_pos1:
    is_game_over = True
else:
    is_enemie_x_pos += 1
    is_enemie_x_pos1 += 1
 """
###########################FOR#####################
is_game_over = False
p_e_pos = 2
e_pos = 3
end_pos = 10


while not is_game_over:
    print(p_e_pos)
    print(e_pos)
    if p_e_pos == e_pos:
        print('Lose')
        is_game_over = True
    elif p_e_pos == end_pos:
        print('win')
        is_game_over = True
    else:
        p_e_pos += 3
        end_pos += 1

x_pos = 5
movements = [1, 2, 3, 4, 5]

for movement in movements:
    x_pos += movement
print(x_pos)

