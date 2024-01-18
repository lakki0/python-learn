
# str1 = "Apple"
str1 = "Hello World"
dict_ = dict()

for char in str1:
    count = str1.count(char)
    dict_[char] = count

print(dict_)



# count_alpha = 0
# count_num = 0
# count_symbol = 0

# def counts(str):
#     global count_symbol,count_alpha,count_num
#     for i in str:
#         if i.isalpha():
#             count_alpha += 1
#         elif i.isdigit():
#             count_num += 1
#         else:
#             count_symbol += 1
#     print("count alphabets ",count_alpha)    
#     print("count numbers ",count_num)            
#     print("count symbols ",count_symbol)            
        

# string1 = "[Version 10.0.22621.2861]"

# counts(string1)
