

def modp(n: int, p: int):
    if p == 1:
        return 0
    else:
        return pow(2, n, p)

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1
<jupyter_output>
3
2
1
8
1
<jupyter_text>
Exercise 2: Write a function that takes as input a positive integer n and returns the smallest prime number that is not less than n.
<jupyter_code>
