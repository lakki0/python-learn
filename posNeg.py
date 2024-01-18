
def posNegative(a):
    neg_count,pos_count = 0,0
    for i in a:
        if i<0:
            neg_count += 1
        else:
            pos_count += 1   
    print("neg : ",neg_count)
    print("pos : ",pos_count) 

list1 = [2, -7, 5, -64, -14]
list2 = [-12, 14, 95, 3]

posNegative(list1)
posNegative(list2)