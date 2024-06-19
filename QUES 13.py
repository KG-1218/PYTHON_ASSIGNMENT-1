#QUES1 13. INPUT BIRTH YEAR AND CALCULATE AGE

birth_year=int(input("enter your birth year"))
birth_month=int(input("enter your birth month"))
birth_day=int(input("enter your birth day"))
present_year=int(input("enter your present year"))
present_month=[31,30,31,30,31,30,31,31,30,31,30,31]
present_day=int(input("enter your present day"))   
if (birth_month > present_month and birth_day >=present_day):
    age=(present_year-birth_year,"years",present_month-birth_month,"months",present_day-birth_day,"days")
elif(birth_month > present_month and birth_day<present_day):
    age=(present_year-birth_year,"years",present_month-birth_month-1,"months",present_day-birth_day,"days")