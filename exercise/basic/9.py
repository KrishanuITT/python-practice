# Check Palindrome Number

def check_palindrome(num):
    org = num
    rev = 0
    while num > 0:
        r = num % 10
        rev = rev * 10 + r
        num = num // 10
    
    return org == rev


print(check_palindrome(12321))
print(check_palindrome(1234))