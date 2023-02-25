count = 0
kmax = -1
with open ('14.txt') as f:
    let = f.readline().replace('C','S').replace('D','S').replace('F','S').replace('A','G').replace('O','G')
    let = let.replace('SG',"*")
    for i in let:
        if i == '*':
            count +=1
            kmax = max(count,kmax)
        else:
            count = 0
print(kmax)
