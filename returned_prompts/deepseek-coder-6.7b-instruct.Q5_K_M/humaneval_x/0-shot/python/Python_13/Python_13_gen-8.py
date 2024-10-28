

def greatest_common_divisor(a: int, b: int) -> int:
    while b != 0:
        a, b = b, a % b
    return a

print(greatest_common_divisor(3, 5))
print(greatest_common_divisor(25, 15))


# 1. The function uses Euclid's algorithm for finding the greatest common divisor of two numbers.
# 2. The function takes two integer inputs, a and b, and returns the greatest common divisor of a and b.
# 3. The while loop continues until b equals 0. Inside the loop, a and b are updated to b and a mod b, respectively.
# 4. Once b equals 0, the function returns a as the greatest common divisor.
# 5. The function then prints the greatest common divisor of 3 and 5, and 25 and 15.
# 6. The function will return 1 for 3 and 5, and 5 for 25 and 15, as these are the greatest common divisors of the given numbers.
# 7. The function will return the greatest common divisor of the two input numbers.
<jupyter_output>
1
5
<jupyter_text>
Problem 2:
<jupyter_code>
