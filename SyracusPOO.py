import numpy as np


class Syracuse:
    def __init__(self,number1,number2):
        self.N=number1
        self.n=number2

    def calcul(self):
        f=open("output.txt","w")
         
        print (self.N)
        f.write(str(self.N)+'\n')

        i = 0
        for i in range (1,self.n + 1): 

            if self.N % 2==0: 
                self.N = self.N//2 
            else: 
                self.N = self.N*3 + 1 
            
            print(self.N)
            f.write(str(self.N)+'\n')

datatext=np.loadtxt(fname="data.txt")
print(datatext)
       
print("Syracuse en POO:")

N=int(datatext[0])
n=int(datatext[1])

test=Syracuse(N,n)
test.calcul()