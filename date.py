day =int(input("Enter day"))
month =int(input("enter month")) 
year =int(input("Enter year"))

if (month == 1 or month == 3 or month ==5 or month ==7 or month ==8 or month ==9 or month ==11):

 print("Month has 31 days")

elif (month ==2) and (year%4==0):
 print("month has 29 days")
elif (month ==2) and (year%4!=0):
 print("Month has 28 days") 

else:
    print("month has 30 days")
