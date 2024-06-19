#QUES 21. COUNTS THE OCCURANCE OF A SPECIFIC ELEMENT IN A LIST

list=[2,3,4,5,6,3,2,5,2]
el=int(input("enter specific element that to be count"))
count=0
for i in list:
    if (i==el):
        count+=1
print(count)