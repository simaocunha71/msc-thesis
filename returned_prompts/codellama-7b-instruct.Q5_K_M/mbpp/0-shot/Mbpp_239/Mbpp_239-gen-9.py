"""
The number of possible sequences of length n that meet the condition is given by the closed form formula:

C(n, 1) * C(m - 1, 1) + C(n, 2) * C(m - 2, 2) + ... + C(n, n) * C(m - n, n)

where C(n, k) is the binomial coefficient that counts the number of ways to choose k items from n items without order.
"""
