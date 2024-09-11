def noprofit_noloss(amount,cost_price):
    if amount > cost_price:
        return True
    else:
        return False

# assert noprofit_noloss(1500,1200)==False



"""
Write a function to check whether a number is a palindrome or not
assert is_palindrome(1221)==True
"""

B:
def is_palindrome(num):
    if num == int(str(num)[::-1]):
        return True
    else:
        return False

# assert is_palindrome(1221)==True



"""
Write a function to check whether a number is prime or not
assert is_prime(10)==False
"""

C:
def is_prime(num):
    if num < 2:
        return False
    for i in range(2,num):
        if num%i==0:
            return False
    return True

# assert is_prime(10)==False



"""
Write a function to check whether a string is a pangram or not
assert is_pangram("The quick brown fox jumps over the lazy dog")==True
"""

D:
def is_pangram(sentence):
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for i in alphabet:
        if i not in sentence.lower():
            return False
    return True

# assert is_pangram("The quick brown fox jumps over the lazy dog")==True



"""
Write a function to check whether a number is odd or even
assert is_odd(12)==False
"""

E:
def is_odd(num):
    return num%2==0

# assert is_odd(12)==False



"""
Write a function to check whether a number is a perfect square or not
assert is_perfect_square(28)==False
"""

F:
def is_perfect_square(num):
    if num < 0:
        return