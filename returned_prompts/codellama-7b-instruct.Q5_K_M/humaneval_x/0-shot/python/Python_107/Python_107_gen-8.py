
class Solution:
    def even_odd_palindrome(self, n):
        # Write your code here
        # count even and odd palindrome
        count_even, count_odd = 0, 0
        for i in range(1, n+1):
            if str(i) == str(i)[::-1]:
                if i % 2 == 0:
                    count_even += 1
                else:
                    count_odd += 1
        return (count_even, count_odd)