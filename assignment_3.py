# n = int(input("enter the number : "))
# p = int(input("enter the power : "))

# def Num_power(val,p):
#     return val**p

# print(Num_power(n,p))


# --------- task 2------------

# Given a number and its base, the task is to convert the given number into its corresponding decimal number. The base of number can be anything like digits between 0 to 9 and A to Z. Where the value of A is 10, value of B is 11, value of C is 12 and so on.
# Input : '1011'

# base = 2

# Output : 11

inp = '1011'
base = 2

def covert_to_num(i,b):
    return int(i,b)

print(covert_to_num(inp,base))