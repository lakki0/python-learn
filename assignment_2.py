# -------- task 1 ----------
# write a python program to remove the ith character from the string

str1 = "This is a python language"
index = int(input("enter the i'th character that want to remove : "))

str2 = str1[:index]+str1[index+1:]
print(str2)


# -------- task 3 ----------

# str1 = "my name is surendra"

# updated_str = str1.split(" ")
# # print(updated_str)
# str2 = ""

# for word in updated_str[::-1]:
#     str2 += word+" "
    
# print(str2)



# -------- task 2 ----------
# Given a string. The task is to print all words with even length in the given string.

# s = "This is a python language"

# updated_str = s.split(" ")
# str2 = ""

# for word in updated_str:
#     if len(word)%2==0:
#         str2 += word+" "
        
# print(str2)