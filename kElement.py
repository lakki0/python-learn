list1 = (8,3,1,6,2,9,4,7,5)
k = int(input("enter the k value : "))

val = sorted(list1)
up_val = val[:k]
val_2 = sorted(list1,reverse=True)
up_val_2 = val_2[:k]

if k<=0:
    print("please inter greater than 0 value")
else:
    print(tuple(up_val+up_val_2))












