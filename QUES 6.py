#QUES 6. READS THE CONTENT OF A FILE AND PRINT IT TO CONSOLE

file1=open('trial.txt','r')
line=file1.readline()
while(line!=""):
    print(line)
    line=file1.readline()
#file1.close()