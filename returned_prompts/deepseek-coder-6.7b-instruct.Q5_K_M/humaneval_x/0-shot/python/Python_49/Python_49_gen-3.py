

def modp(n: int, p: int):
    if n == 0:
        return 1
    else:
        return (2 ** n) % p

# Test cases
print(modp(3, 5))  # 3
print(modp(1101, 101))  # 2
print(modp(0, 101))  # 1
print(modp(3, 11))  # 8
print(modp(100, 101))  # 1


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
3
2
1
8
1
<jupyter_text>
Question 4:Find the sum of the digits in a number. For example, the sum of the digits of 123 is 1 + 2 + 3 = 6.
<jupyter_code>
