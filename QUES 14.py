#QUES 14 READS MULTIPLE LINE OF INPUT FROM USER UNTIL THEY ENTER AN EMPTY LINE THEN PRINT ALL LINES
lines=[]
print("enter:")
while True:
    line=input()
    if line:
        lines.append(line)
    else:
        print("end!!!!")
        break    