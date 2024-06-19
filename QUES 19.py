#QUES 19. REMOVES ALL PUNCTUATIONS FROM GIVEN STRINGS

punc= '''~!@#$%^&*()[-_+=]|}{:;\'"/.,<>?'''
str1=input("enter string")
i=" "
for el in str1:
    if el not in punc:
        #str1=str1.replace(punc, i)
        i=i+el
print(i)