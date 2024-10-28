
def even_odd_palindrome(n):
    count_even = 0
    count_odd = 0
    for i in range(1, n):
        if is_palindrome(i):
            if i % 2 == 0:
                count_even += 1
            else:
                count_odd += 1
    return (count_even, count_odd)

def is_palindrome(n):
    return str(n) == str(n)[::-1]

class Solution:
    def evenOddPalindrome(self, n: int) -> List[int]:
        count_even = 0
        count_odd = 0
        for i in range(1, n):
            if is_palindrome(i):
                if i % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
        return [count_even, count_odd]

class Solution:
    def evenOddPalindrome(self, n: int) -> List[int]:
        return [sum(1 for i in range(1, n) if is_palindrome(i) and i % 2 == 0),
                sum(1 for i in range(1, n) if is_palindrome(i) and i % 2 == 1)]
