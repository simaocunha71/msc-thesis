
def divisors(n):
    divs = [1]
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            if n // i == i:
                divs.append(i)
            else:
                divs.extend([i, n // i])
    return divs

def amicable_numbers_sum(limit):
    numbers = [0] * (limit+1)
    for i in range(1, limit+1):
        numbers[i] = sum(divisors(i))
    return sum(i for i in range(1, limit+1) if i < numbers[i] and numbers[numbers[i]] == i)

print(amicable_mbumbers_sum(999)) # 504

"""
The function `divisors(n)` calculates all divisors of `n`.
The function `amicable_numbers_sum(limit)` calculates all amicable numbers from 1 to `limit`.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 2:**Write a Python function to find the longest common prefix string amongst an array of strings. If there is no common prefix, return an empty string "".
<jupyter_code>
