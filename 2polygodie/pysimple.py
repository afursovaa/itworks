import PySimpleGUI as sg

sg.theme('LightBlue2')  # Set the theme
s= ['1', '2', '3', '4', '5', '6', '7', '8', '9', '12', '13', '14', '15', '16', '17', '23', '24', '25', '26', '27']
a=[
# 1
'''
  1) Разделит пункты по количеству дорог
  2) Сопоставить пункты с названиями пункатов из таблицы в соответствии с количеством дорог
  3) Выявить возможные расположения пунктов
  4) Найти подходящий
''',
# 2
'''for y in range(2):
   for z in range(2):
   
      for w in range(2):
      
         if (not(y<=x) or (z<=w) or not(z))==False:
         
            print(x, y, z, w)''',
# 3
'''На все таблицы поставить фильтр''',
# 4
'''  1) Рассписать двоичное дерево
  2) занести в него известные данные
  3)Соотнести кол-во вариантов с кол-вом символов, начинаем с самого минимального кода''',
# 5
'''   chislo=''
   num=(bin(i)[2:])   
   if num.count('1')%2==0:
       chislo='10'+num[2:]+'0'
   if num.count('1')%2!=0:    
       chislo='11'+num[2:]+'1'        
   if int(chislo,2)>40:    
       print (i, int(chislo,2))        
       break''',

# 6
'''from turtle import *
left(90)
for i in range(7):
    forward(300)
    right(120)
pu()
for x in range(1, 9):
    for y in range(1, 10):
        goto(x*30,y*30)
        dot(5)
done()''',

# 7
'''1)сгенерировать все возможные варианты чисел(for/product)
2)проверить строчку на условия
3)выводим счетчик значений''',

# 8
'''
  1) создаем все возможные варианты искомой величены
  2) Проверяем, есть ли в последовательности выполнение условий
  3) вывод подчета
''',

# 9
'''
spisok=[]
for num in range(2,1000):
  n=0
  for delit in range (2,100):
    if num%delit==0 and x<i: n+=1
  
  if n==0:spisok.append(num)
        
flag=False
for i in spisok:
    for y in range (100):
        if y*4+117==i and flag==False:
            print(y, i)
            flag=True
''',
# 10
'',
# 11
'',
# 12
'',
# 13
'''
  1) Стартовая позиция маркируется единицей
  2) учитываем логику движения, следить за путями в которые попасть не можем, следовать маршруту
  3) алализируем пункты, в которые можно попасть по одной дороге
  4) продолжаем анализировать пункты, считая количество возможных вариантов попадения в эти пункты
  5) складываем общее количество вариаций 
''',
# 14
'''
alph='0123456789abcde'
for x in alph:
    f=int(f'123{x}5',15)+int(f'1{x}233',15)
    if  f%14 ==0:
        print(f//14)
        break
''',
# 15
'''
for a in range(1, 1000):
   if all((x%2 == 0) <= (x%3 != 0) or (x + a >= 100) for x in range(1, 1000)):
      print(a)
      break
''',
# 16
'''
itog1=itog2=1
for x1 in range(1,2024):
    itog1=itog1*x1
for x2 in range(1,2021):
    itog2=itog2*x2
print(itog1/itog2)
''',
# 17
'''
with open('17.txt') as f:
    nums=[int(x) for x in f]
    maxi=[]
    s=[]
   
    for i in range(len(nums)):
      if nums[i]%10==3:
         maxi.append(nums[i])
    maximum=0
    for i in range(len(nums)-1):
        a=abs(nums[i])%10
        b=abs(nums[i+1])%10
        if ((a==3) and (b!=3)) or ((a!=3) and (b==3)):
        if (nums[i]**2+nums[i+1]**2) >= max(maxi)**2: 
            s.append(nums[i]+nums[i+1])
            if nums[i]**2+nums[i+1]**2>maximum:
                maximum=nums[i]**2+nums[i+1]**2
print(len(s), maximum)
''',
 #18
  '',
#19
  '''
  1)Точка входа (цель)
  2)Расписываем дерево на 4 хода
  3)Считаем по условию задачи в каком порядке работают игроки
  ''',
 #20
  '''
  
  ''',
 #21
  '''
  
  ''',
  #23
  '''
from itertools import product
def f23(x,y,z):
    count=0
    for i in range(1,z):
        nums=product('12',repeat=i)
        for numb in nums:
            #numb=''.join(n)
            a=x
            if x==10 and numb.count('2')>1:continue
            for ii in numb:
                if a==17: break 
                if ii=='1':a+=1
                elif ii=='2' :a*=2
            if a==y: count+=1
    return count
                
print(f23(1,10,10)*f23(10,35,25))
''',
'''
#24
with open('24.txt') as f:
    s=f.readline().replace('C','S').replace('D','S').replace('F','S')
    s=s.replace('A','G').replace('O','G')
    s=s.replace('SG','*')
    k=kmax=0
    for i in s:
        if i=='*'
            k+=1
            kmax=max(k,kmax)
        else:k=0
print(kmax)
''',
'''
#25
for i in range(2023,10**10,2023):
    num=str(i)
    if num[0]=='1' and num[2:6]=='2139' and num[-1]=='4':
        print(i,i//2023)
''',
'''
#26
with open('26.txt') as f:
    s=[int(x) for x in f]
    s=sorted(s[1:],reverse=True)
    k,mini=1,s[0]
    for i in range(1,len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
print(k,mini)
''',
'''
#27
  А)
  1) Загрузить данные из файла, удалить первый элемент
  2) Создать переменную по длине списка
  3) Удвоить список, чтобы на его основе создавать другой рабочий список, обнулить стоимость
  4) В цикле создать список на основе среза сдвоенного списка
  5) Используя созданный список мы считаем соимость первого элемента по формуле
  6) смещая срез, находим стоимости всех пунктов
  7) в случии кольцевой дороги индексы пересчитываются на убывание(для этого нужно создать новую переменную)
  8) стоимости пунктов накапливаются в списке
  9) в качестве ответа выдается индекс минимального элемента списка + 1 (км нумеруются с 1)
  
  Б)
  1) в отличие от А цикл организуем не по длине списка, по диапозону, в аргументах которого есть старт, финиш и шаг
  2) используем не подход перебором, а замер равнораспределенных выборочных км
  3) организум глобальный цикл, в котором значения старт, финиш и шаг будут изменятся
  4) после каждого глобального прохода уменьшаем границы диапозона, уменьшая их
  5) условия выхода из бесконечного цикла : повторение ответа два раза при шаге 1
  6) если шаг = 0, то шаг устанавливается 1
  7) целесообразно на каждом проходе писать новые значения старта, финиша и шага
  8) границы диапозона астарт и финиш определяются по минимальному километражу минус шаг и плюс шаг соответственно
  9) после пересчета старта и финиша пересчитываем шаг
  10) целесообразно брать 20 замеров на диапозон 
  
''']
  
]
# Define the layout
layout = [ [sg.Combo(s, default_value=s[0], s=(15,22), enable_events=True, readonly=True, k='-COMBO-', key='Combo'),
          sg.Output(s=(40,10), key='outputt')],
          [sg.Button('Process Input', font=('Arial', 12), button_color=('white', '#4CAF50'), key='process'),
           sg.Button('Someth', font=('Arial', 12), button_color=('white', '#4CAF50'), key='button')]]

# Create the window
window = sg.Window('справочник ЕГЭ; Шаманина', layout)

# Event loop
while True:
    event, values = window.read()

    # Exit the app when the window is closed
    if event == sg.WINDOW_CLOSED:
        break

    # Process the input and update the output when the button is clicked
    if event == 'process':
        input_text = values['input']
        choice=a[int(values['Combo'])-1]
        #print(choice)
        window['input'].update('')
        window['output'].update(input_text)
        window['outputt'].update('')
        window['outputt'].update(choice)
    if event == 'button':
        break

# Close the window
window.close()
