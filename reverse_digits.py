number = int(input("ENter number"))
reverse = 0
while(number > 0):
    c =  number %10
    reverse = ((reverse *10) + c)
    number = number//10
    
print(reverse)
