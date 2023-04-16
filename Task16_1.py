N= [1,2,3,4,5,4,3,3]
x=int(input("Введите искомое число х = "))
count = 0
for i in N :
    if i == x:
        count += 1
print(count)