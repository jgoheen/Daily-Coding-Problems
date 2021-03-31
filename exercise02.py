'''

Good morning! Here's your coding interview problem for today.
This problem was asked by Uber.
Given an array of integers, return a new array such that each element at index i of the new array 
is the product of all the numbers in the original array except the one at i.
For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. 
If our input was [3, 2, 1], the expected output would be [2, 3, 6].
Follow-up: what if you can't use division?

'''

import random

'using a list as an array'
def getIntList(k):
    intList = []
    for i in range(k):
        n = random.randint(1,10)
        intList.append(n)
    return(intList)

myList = getIntList(5)
print(myList)

newList = []
tempListA = []
tempListB = []
tempListC = []
j = 0
k = 0
prod = 1
prodA = 1
prodB = 1

for i in range(len(myList)):
    tempListA = myList[:i]
    tempListB = myList[i+1:]
    for x in range(len(tempListA)):
        prodA = prodA * tempListA[x]
    for x in range(len(tempListB)):
        prodB = prodB * tempListB[x]
    prod = prodA * prodB
    newList.append(prod)
    prod = 1
    prodA = 1
    prodB = 1

print(newList)
