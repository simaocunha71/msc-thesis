def reverse_Array_Upto_K(arr,k):
    left = 0
    right = k-1
    while left < right:
        arr[left],arr[right] = arr[right], arr[left]
        left += 1
        right -= 1
    return arr

reverse_Array_Upto_K([1, 2, 3, 4, 5, 6],4)

"""
The above function works on the concept of swapping the elements from both ends of the array. Here we are swapping the elements from the start of the array till the position k and then from the end till the position k. This would reverse the array till the position k.
"""

"""
Time Complexity: O(n)
Space Complexity: O(1)
"""

# Python3 program to print
# all prime factors of a number


def primeFactors(n):
    # Print the number of 2s that divide n
    while n % 2 == 0:
        print(2,end=" ")
        n = n / 2

    # n must be odd at this point. So we can skip one element (Note i = i +2)
    for i in range(3, int(n ** 0.5) + 1, 2):

        # While i divides n, print i and divide n
        while n % i == 0:
            print(i, end=" ")
            n = n / i

    # This condition is to handle the case when n is a prime number
    # greater than 2
    if n > 2:
        print(n)

# Driver program to test the above function
n = 12
primeFactors(n)

"""
Explanation:
The above program finds all the prime factors of a given number. It starts with the lowest prime number, 2, and checks if the number is divisible by 2. If it is divisible by 2, it prints 2 and divides the number by 2. It keeps on doing so until the number is no longer divisible by 2. After that, it checks for the next odd prime number and follows the same procedure until the number is no longer divisible