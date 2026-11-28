numbers=[1,23,56,77,89,7,4,8,3,11,15]

even=[]
odd=[]

for i in numbers:
    if i%2==0:
        even.append(i)
    else:
        odd.append(i)

print("Original list: ",numbers)
print("Even list: ",even)
print("Odd list: ",odd)