numbers=[20,30,40,50,20,30,10,30,80,40,40,20,50,60]
num=[]
for i in numbers:
    if i not in num:
        num.append(i)
print(num)