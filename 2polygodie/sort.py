s = [100, 0, 1000, 10, 2, 4]
a = 1
while a == 1:
    
    for i in range(len(s)-1): 
        if(s[i] > s[i+1]): #если текущее число больше следующего, то меняем их местами
            s[i], s[i+1] = s[i+1], s[i]
    for i in range(len(s)):
        print(s[i])
    if all(s[i] <= s[i + 1] for i in range(len(s)-1)): #проверка(все ли числа в порядке возраствния?)
        a = 2
