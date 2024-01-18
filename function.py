# x = int(input("enter the value : "))
# y = 1
# for i in range(1,x+1):
#     y = y*i
    
# print(y)

# for i in range(10,100):
#     if(i%2==0):
#         print(i,end=" ")
        
#     else:
#         print("-",end=" ")


def factorial(num):
    fact = 1
    if(num==0):
        return fact
    else:
        for i in range(1,num+1):
            fact=fact*i
            i+=1
        return fact


print(factorial(5))
print(factorial(10))
