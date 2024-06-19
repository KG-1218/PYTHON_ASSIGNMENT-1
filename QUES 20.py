#QUES 20 TAKE LIST OF NUUMBERS AND RETURN THEIR SUM

list=[]
n=int(input("enter n:"))
#n=len(list)
print("enter numbers")
sum=0
for i in range(0,n):
    e=int(input())
    list.append(e)
print(list)
for el in list:
    sum=sum+el
print(sum)