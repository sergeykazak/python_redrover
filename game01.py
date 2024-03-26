#Ghost Game
from random import randint
print("Сыграем в игру Дом с привидениями")
feeling_brave = True
score = 0
while feeling_brave:
    ghost_door = randint(1, 2)
    print('Перед тобой три двери....')
    print('Приведение за одной из дверей...')
    print('Какую из дверей ты откроешь?')
    door_num = int(input('1, 2, или 3 ?'))
    if door_num == ghost_door:
        print('Мамааааа!!!! Приведение!!! Убегаааееееммм')
        feeling_brave = False
    else:
        print('Тут приведения нет!!!')
        print('Выбери следующую дверь')
        score = score + 1
print("Убегаемммммм!!!")
print(f'Игра окончена! Твой результат {score}')
