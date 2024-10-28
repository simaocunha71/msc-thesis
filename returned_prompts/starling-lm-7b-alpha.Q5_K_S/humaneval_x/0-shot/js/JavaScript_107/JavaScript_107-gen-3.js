To solve this problem, we can iterate through each number from 1 to n, and check if the number is a palindrome. If it is, we need to determine if it's even or odd.

Here is a step-by-step explanation of the solution:

1. Create an empty array to store the count of even and odd palindromes.
2. Initialize two variables, evenCount and oddCount, to keep track of the number of even and odd palindromes.
3. Iterate through each number from 1 to n.
4. For each number, check if it's a palindrome. We can do this by comparing the number to its reverse. For example, if the number is 121, it's a palindrome because it's the same when reversed.
5. If the number is a palindrome, check if it's even or odd. We can do this by checking if the number is divisible by 2. If it is, it's even; otherwise, it's odd.
6. Increment the count of even or odd palindromes based on the result of step 5.
7. After iterating through all the numbers, return the array containing the count of even and odd palindromes.

Here's a Python implementation of the solution:

def evenOddPalindrome(n):
    even = 0
    odd = 0
    for i in range(1, n+1):
        if str(i) == str(i)[::-1]:
            if i % 2 == 0:
                even += 1
            else:
                odd += 1
    return [even, odd]

This function will return a list with the count of even and odd palindromes in the range (1, n), inclusive.

For example, if you call evenOddPalindrome(3), it will return [1, 2] because there is 1 even palindrome (2) and 2 odd palindromes (1 and 3) in the range (1, 3).

Similarly, if you call evenOddPalindrome(12), it will return [4, 6] because there are 4 even palindrom