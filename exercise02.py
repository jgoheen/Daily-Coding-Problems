'''
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''
from random import random
from random import seed
from random import randint

# generate a random list of numbers under 10 and under length 4 and print it to the screen
a = []
for i in range(0, 4):
    a.append(randint(0,10))
print('a = ', a)

updatedList = []

i = 0
while i < len(a):
  tempList=a[:i] + a[i+1:]
  print('tempList = ', tempList)
  p=1
  for n in tempList:
    p *= n 
  updatedList.append(p)
  i = i + 1
  
a[1]=20
print('updatedList = ', updatedList)
