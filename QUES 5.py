#QUES 5.TAKES STRING AS INPUT AND WRITES TO TEXT FILE

temp=input("enter string")
with open('trial.txt','w') as trial:
    trial.write(temp)
