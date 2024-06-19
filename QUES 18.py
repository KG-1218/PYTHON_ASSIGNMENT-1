#QUES 18. CHECKS IF TWO STRINGS ARE ANAGRAMS OF EACH OTHER
str1=input("enter string")
str2=input("enter string")
if(sorted(str1)==sorted(str2)):
    print("anagrams")
else:
    print("not anagrams")