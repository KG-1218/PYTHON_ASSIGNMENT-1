#QUES 12.calculate sum of digits of given number
digit=int(input("enter digit"))
num=0
while digit!=0:
    num+=digit%10
    digit=int(digit/10)
print("sum of all digits is:",num)