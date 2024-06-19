#QUES 26. CHECKS IF STRING START WITH GIVEN PREFFIX OR ENDS WITH A GIVEN SUFFIX

str=input("enter string: ")
preffix=input("enter preffix: ")
suffix=input(("enter suffix: "))
if (str.startswith(preffix)):
    print("preffix present")
if (str.endswith(suffix)):
    print("suffix present")