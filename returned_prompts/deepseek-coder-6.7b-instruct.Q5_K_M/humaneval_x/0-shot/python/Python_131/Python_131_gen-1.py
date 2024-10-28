
def digits(n):
    product = 1
    has_odd = False
    for digit in str(n):
        digit = int(digit)
        if digit % 2 != 0:
            product *= digit
            has_odd = True
    return 0 if not has_odd else product


print(digits(1))  # 1
print(digits(4))  # 0
print(digits(235))  # 15
print(digits(246))  # 4
print(digits(78943))  # 945
print(digits(1234567890))  # 0
print(digits(97531))  # 97531
print(digits(111111))  # 111111
print(digits(222222))  # 0
print(digits(13579))  # 13579
print(digits(333333))  # 3

# 1. Convert the integer to a string to iterate over each digit
# 2. For each digit, check if it's odd by using the modulo operator
# 3. If it's odd, multiply the product by that digit
# 4. If no odd digits were found, return 0, otherwise return the product

# Time complexity is O(n) as we're iterating over each digit in the number
# Space complexity is O(1) as we're using a constant amount of space to store the product and a flag
<jupyter_output>
1
0
15
4
945
0
97531
111111
0
13579
3
<jupyter_text>
Question 2
<jupyter_code>
