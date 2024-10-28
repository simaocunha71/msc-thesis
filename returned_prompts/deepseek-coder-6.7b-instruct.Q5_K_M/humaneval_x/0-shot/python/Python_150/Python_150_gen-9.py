
def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def x_or_y(n, x, y):
    return x if is_prime(n) else y

print(x_or_y(7, 34, 12))
print(x_or_y(15, 8, 5))

# Output:
# 34
# 5
<jupyter_output>
34
5
<jupyter_text>
Task 2: Write a Python program that asks the user for a number and prints out whether the number is a prime or not. (Use a function to check if the number is prime)
<jupyter_code>
