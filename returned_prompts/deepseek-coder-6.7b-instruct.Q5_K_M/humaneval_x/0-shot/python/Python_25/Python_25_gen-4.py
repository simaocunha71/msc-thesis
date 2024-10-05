from typing import List

def factorize(n: int) -> List[int]:
    factors = []
    divisor = 2
    while(divisor <= n):
        if (n % divisor) == 0:
            factors.append(divisor)
            n = n / divisor
        else:
            divisor += 1
    return factors

print(factorize(8))  # [2, 2, 2]
print(factorize(25))  # [5, 5]
print(factorize(70))  # [2, 5, 7]

In this solution, we start by defining an empty list to hold our prime factors. We then start a while loop that will run as long as our divisor is less than or equal to the input number. Inside the loop, we check if our input number is divisible by our divisor. If it is, we append our divisor to our factors list and update our input number. If it isn't, we increment our divisor by 1. Finally, we return our factors list.

Please note that this solution assumes that the input number is positive and greater than 1. If the input number is 0 or negative, you may want to add error checking to handle those cases.

Also, the time complexity of this solution is O(n), because in the worst case, it will loop n times.

Finally, this solution does not handle perfect squares. If you want to handle perfect squares, you may want to add a special case to handle that.

This solution is correct and efficient for small inputs, but it may not be efficient for large inputs. If you need to handle very large inputs, you may want to consider a different algorithm.
