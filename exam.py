
n=int(input('enter the number')) 
for i in range (1,n):
    for j in range (1,n-i):
        print(' ',end="")
    for k in range(n-i,n):
        print('*',end="")
    for l in range (1,i):
        print('*',end="")
    print('\n')
    
for i in range (2,n):
    for j in range (n-i,n-1):
        print(' ',end="")
    for k in range(1,n-i):
        print('*',end="")
    for l in range (1,n-i+1):
        print('*',end="")
    print('\n')
    

    
