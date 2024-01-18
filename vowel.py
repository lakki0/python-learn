# vowels = "aeiou"
# string = "yogi & lakki"

# for char in string:
#     if char in vowels:
#         string = string.replace(char,"z")
        
# print(string)

value = int(input("enter the number: "))
count = 0
while value>0:
    count +=1
    value = value//10

print(count)


