#QUES 11. GENERATE FIRST N NUMBERS IN FIBONACCI SEQUENCE
a=0
b=1
n=int(input("enter n:"))
print("n numbers are: \n",a,"\n",b)
for el in range(1,(n-1)):
    new=a+b
    a=b
    b=new
    print(new)