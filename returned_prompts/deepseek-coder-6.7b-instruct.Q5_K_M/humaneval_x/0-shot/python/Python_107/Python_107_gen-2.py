
    def is_palindrome(num):
        return str(num) == str(num)[::-1]

    def even_odd_palindrome(n):
        even_count = 0
        odd_count = 0
        for i in range(1, n + 1):
            if is_palindrome(i):
                if i % 2 == 0:
                    even_count += 1
                else:
                    odd_count += 1
        return (even_count, odd_count)

print(even_odd_palindrome(3))
print(even_odd_palindrome(12))



The function `is_palindrome` checks whether a number is a palindrome or not. It does so by converting the number to a string and comparing it with the reversed string. The function `even_odd_palindrome` iterates from 1 to n and for each number, it checks whether the number is a palindrome or not. If the number is a palindrome, it further checks whether the number is even or odd and increments the count accordingly. It returns a tuple of two counts, the first one being the count of even palindromes and the second one being the count of odd palindromes.


The time complexity of the solution is O(n) and the space complexity is O(1) as it uses a constant amount of space.


The function `even_odd_palindrome` works as expected for the given examples.
'''

# Solution 2:
'''
