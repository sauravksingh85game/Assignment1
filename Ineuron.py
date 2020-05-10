# -*- coding: utf-8 -*-
"""
Created on Wed May  6 21:11:25 2020

@author: 714404
"""
#2.
m=[]
for x in range(1500,3201):
    if (x%7==0) and (x%5!=0):
       m.append(x) 
print(*m,sep=",")        
        
#3.
a=input()
b=input()
print(b+" " +a)
#4.
d=12
r=d/2
V=4/3*22/7*(r**3)
print(round(V,2))

#5
a=input()
a.split(",")   

#6
for i in range(1,6):
      for j in range(i):
            if(j<=i):
              print("* ",end=" ")
      print('')
for i in range(5,0,-1):
      for j in range(i):
            print("* ",end=" ")
      print('')    

#7
a=input()

print (a[:: -1])
