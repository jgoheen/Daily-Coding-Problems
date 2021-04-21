'''

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.

'''

def recurringChar(s):
    i = 0
    j = 1
    while j < len(s):
        if s[i] == s[j]:
            return((s[i]))
            break
        i += 1 
        j += 1 
    return "null"
    
print(recurringChar("acbbac"))
print(recurringChar("abcdef"))
print(recurringChar("abcdefczaldgerald"))
print(recurringChar("springbuzzard"))
