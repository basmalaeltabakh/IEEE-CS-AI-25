def Common(lst1,lst2):
    commonElements = set()
    for item in lst1:
        if item in lst2:
            commonElements.add(item)
    return commonElements


lst1 = {2 , 5 , 7 ,10 ,12 , 1 , 4 , 6}
lst2=  {6 , 3 , 9 , 2 , 8 , 14 ,1,10}
result = Common(lst1 , lst2)
print (result)