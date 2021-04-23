'''
Given a string, determine whether any permutation of it is a palindrome.
For example, carrace should return true, since it can be rearranged to form racecar, 
which is a palindrome. daily should return false, since there's no rearrangement that can form a palindrome.
'''

def palindromeCheck(string_check):
    if (len(string_check) % 2) == 0:
        for i in string_check:
            if string_check.count(i) % 2 == 0:
                continue
            else:
                return "false"
        return "true"
    else:
        num_of_odd_chars = 0
        for i in string_check:
            if string_check.count(i) % 2 == 0:
                continue
            if string_check.count(i) % 2 == 1:
                num_of_odd_chars += 1 
        if num_of_odd_chars % 2 == 0:
            print(num_of_odd_chars)
            return "false"
        else:
            return "true"

s1 = "carrac"
s2 = "iiiiiuuuuhhjjkkmmnyny"

print(palindromeCheck(s1))
print(palindromeCheck(s2))
