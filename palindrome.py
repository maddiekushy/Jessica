def palindrome(p):
    if len(p) <= 1:
        return True

    if p[0] != p[-1]:
        return False
    
    return palindrome(p[1:-1])

print(palindrome("racecar"))