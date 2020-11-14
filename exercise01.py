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

# generate a random list of numbers under 10 and under length 10 and print it to the screen
a = []
for i in range(0, 10):
    a.append(randint(0,10))
print('a = ', a)

#generate a random number below 40
k = randint(0,40)
print('k = ', + k)

for x in range(len(a)):
    for y in range(len(a)):
        if a[x] == a[y]:
            continue
        if a[x] + a[y] == k:
            print(str(a[x]) + ' + ' + str(a[y]) + ' = ' + str(k))
            print(True)
            break