x = input("enter your number : ")
total = 0
for i in x:
    total += int(i)**3

# print(total)
if total==int(x):
    print(x,"is a armstrong number")
else:
    print("Not armstrong number")