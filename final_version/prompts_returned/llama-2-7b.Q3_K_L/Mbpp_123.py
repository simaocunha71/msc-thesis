"""
Write a function to sum all amicable numbers from 1 to a specified number.
assert amicable_numbers_sum(999)==504
"""
class Solution:
    def amicable_numbers_sum(self, n):
        amicables = set([])
        for i in range(2,n+1):
            while i % 2 == 0 and i not in amicables:
                amicables.add(i)
            if i%2 != 0:
                amicable_prime_square = i/2
                if amicable_prime_square in amicables:
                    continue
                while True:
                    a = amicable_prime_square+1
                    b = amicable_prime_square - 1
                    if a > n or b < 3:
                        break
                    if (a,b) not in amicables and int(a*b) == n:
                        amicables.add((a,b))
            print(amicable_prime_square)
        return sum([i for i in amicables])