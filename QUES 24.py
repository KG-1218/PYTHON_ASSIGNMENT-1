#QUES 24. MAKE A CALCULATOR THAT TAKES TWO NUMBERS AND OPERATOR AS INPUT AND CALCULATE ITS RESULT

a=int(input("enter first number: \n"))
b=int(input("enter second number: \n"))
op=input("enter operator: ")
if op=='+':
    print(a+b)
if op=='-':
    print(a-b)
if op=='*':
    print(a*b)
if op=='/':
    print(a/b)