with open('26.txt') as f:
    data=[int(x) for x inf]
    s=sorted(s[1:],reverse=True)
    k,mini=1,s[0]

    for i in range(1,len(s)):
        if s[i]+3<=mini:
            mini=s[i]
            k+=1
print(k,mini)
