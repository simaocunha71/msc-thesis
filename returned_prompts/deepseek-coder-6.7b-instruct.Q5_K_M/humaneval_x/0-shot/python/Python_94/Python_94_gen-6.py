
def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = max(i for i in lst if is_prime(i))
    return sum(int(digit) for digit in str(max_prime))

# Tests:
print(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])) # 10
print(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1])) # 25
print(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3])) # 13
print(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6])) # 11
print(skjkasdkd([0,81,12,3,1,21])) # 3
print(skjkasdkd([0,8,1,2,1,7])) # 7

The function skjkasdkd(lst) first defines a helper function is_prime(n) that checks if a number n is prime. Then it finds the maximum prime number in the list lst with max(i for i in lst if is_prime(i)). Finally, it calculates and returns the sum of the digits of the found maximum prime number with sum(int(digit) for digit in str(max_prime)).

This is a Python solution.
"""
</code>
"""

