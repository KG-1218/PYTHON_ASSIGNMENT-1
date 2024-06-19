#QUES 25. COPIES CONTENT OF ONE TEXT FILE TO ANOTHER
with open('trial.txt','r') as trial,open('trial2.txt','a') as trial2:
    for line in trial:
        trial2.write(line)