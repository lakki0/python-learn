a = int(input("enter 1st value "))
b = int(input("enter 2nd value "))

def gcd(a, b): 
    while b: 
        a, b = b, a % b
    return a

print("GCD value is : ",gcd(a,b))