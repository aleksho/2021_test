#1

mysum = 0
for i in range(1,101):
    if i %2 == 0:
        mysum +=i

print(mysum)

#2

s = 'bfgshbkis'

print(s[::-1][1:-2:2])

#3

numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
print(list(filter(lambda x: x% 2 !=0,  numbers)))

#4

mydict = {'one': 1, 'two': 2, 'thee': 3, 'four': 4, 'five': 5}
newdict = {k: v for k, v in mydict.items() if v >=3}
print(newdict)

#5
import random
numbers = [0, 99, 100, 53, 44, 23, 4, 8, 16, 15, 77, 51]
print(random.choice(numbers))

#6
class Animal():
    def voice(self):
        pass
    
class Animal01(Animal):
    def voice(self):
        print('Animal01')
        
class Animal02(Animal):
    def voice(self):
        print('Animal02')
        
class Animal03(Animal):
    def voice(self):
        print('Animal03')
        
A = Animal01()

B = Animal02()
C = Animal03()

print(A.voice(), B.voice(), C.voice())

#7
class Animal():
    child = 0
    def __init__(self):
        Animal.child = self.child + 1
    def all_child():
        print(Animal.child)
    
    num_child = staticmethod(all_child)
       
    def voice(self):
        print('MainClass')
    
class Animal01(Animal):
    def voice(self):
        print('Animal01')
    def mainclass(self):
        return super().voice()
        
class Animal02(Animal):
    def voice(self):
        print('Animal02')
        
class Animal03(Animal):
    def voice(self):
        print('Animal03')
        
A = Animal01()
B = Animal01()
Animal.num_child()
C = Animal03()

A.num_child()

#8
import os

with open('file1.txt', 'w') as f:
    f.write(','.join(map(str,range(20))))
    
with open('file1.txt', 'r') as f:
    line=f.read()
    
revline = line[::-1]

with open('file2.txt', 'w') as f:
    f.write(revline)
    
with open('file2.txt', 'r') as f:
    line2=f.read()
print(line)
print('\n\n')
print(line2)


#9

import os
import subprocess
import sys

def subprint(name):
    for x in range(10,0,-1):
        print(f"Process: {name} Num: {x:02}")
    
subprint('a')
