test 
a = int(input("Nombre à décomposer: "))
b = int(input ("Puissance de 2: "))

i = 0
while a != 0:
    if (a % 2) == 1:
        i = i+b
    b = b*2
    a = a//2
print(i)