def skjkasdkd(lst):
    def is_prime(n):
        if n < 2:
            return False
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                return False
        return True

    max_prime = max([x for x in lst if is_prime(x)])
    return sum(int(digit) for digit in str(max_prime))



# Test cases
print(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3]))  # Output: 10
print(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1]))  # Output: 25
print(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1,9,3]))  # Output: 13
print(skjkasdkd([0,724,32,71,99,32,6,0,5,91,83,0,5,6]))  # Output: 11
print(skjkasdkd([0,81,12,3,1,21]))  # Output: 3
print(skjkasdkd([0,8,1,2,1,7]))  # Output: 7

This function works by first defining a helper function `is_prime` to check if a number is prime. It then uses a list comprehension to find the maximum prime number in the list, and finally returns the sum of the digits of the maximum prime number. The test cases are used to verify that the function produces the expected output.