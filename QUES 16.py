#QUES 16.COUNTS FREQUENCY OF EACH CHARACTER IN A STRING

str=input("enter string")
list={}
for el in str:
    if el in list:
        list[el]+=1
    else:
        list[el]=1  #assigning value(1) for key(el)
print(list)
   # print(el)