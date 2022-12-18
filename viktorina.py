a = ["как зовут Павла Николаевича?", "сколько углов в пятиугольнике?", 'ты стараешься учиться?',
     'айтишник ли ты?', 'синус 30 градусов?']
scores = int(0)
for i in range(len(a)):
    if i == 0:
        answer = (input(f'{a[i]}\n'))
        if answer == "Павел":
            scores += 1
    if i == 1:
        answer = int(input(f'{a[i]}\n   1 - 1\n   2 - 2\n   3 - 5\n   4 - 4\n'))
        if answer == 3:
            scores += 1
    if i == 2:
        answer = input(f'{a[i]}\n')
        if answer == 'да':
            scores += 1
    if i == 3:
        answer = input(f'{a[i]}\n')
        if answer == 'да':
            scores += 1
    if i ==4:
        answer = float(input(f'{a[i]}\n'))
        if answer == 0.5:
            scores += 1
print(f'твоя оценка - {scores}')
