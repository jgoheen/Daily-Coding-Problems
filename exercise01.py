'''
Good morning! Here's your coding interview problem for today.
This problem was recently asked by Google.
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
Bonus: Can you do this in one pass?
'''
import random

listLength = 10
k = random.randint(50,100)

randomList = []

for i in range(listLength):
    n = random.randint(0,100)
    randomList.append(n)

print("k = ", k)
print(randomList)

def sum_to_k(l, k):
    for i in l:
        for j in l:
            if ((i != j) and ((i + j) == k)):
                print("True!")
                print(i, " + ", j, " = ", k)
                return True

print(sum_to_k(randomList, k))
