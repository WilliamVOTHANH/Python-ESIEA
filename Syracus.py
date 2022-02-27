N = int(input("Nombre initial: "))
n = int(input ("Nombre d'iteration: "))
u = N
print (u)
i = 0
for i in range (1,n+1): 

    if u%2==0: 
        u = u//2 
    else: 
        u = u*3 + 1 
    
    print(u)
