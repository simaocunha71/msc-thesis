def sumofFactors(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            if i % 2 == 0:
                sum += i
    return sum

print(sumofFactors(18))
<jupyter_output>
26
<jupyter_text>
2. Write a Python function to find the sum of all divisors of a number.
<jupyter_code>
def sumofDivisors(n):
    sum = 0
    for i in range(1,n+1):
        if n % i == 0:
            sum += i
    return sum

print(sumofDivisors(18))
<jupyter_output>
24
<jupyter_text>
3. Write a Python function to find the factorial of a number.
<jupyter_code>
def factorial(n):
    if n==0:
        return 1
    else:
        return n*factorial(n-1)

print(factorial(5))
<jupyter_output>
120
<jupyter_text>
4. Write a Python function to find the greatest common divisor of two numbers.
<jupyter_code>
def gcd(a,b):
    while b != 0:
        a, b = b, a % b
    return a

print(gcd(18, 48))
<jupyter_output>
6
<jupyter_text>
5. Write a Python function to find the least common multiple of two numbers.
<jupyter_code>
def lcm(a,b):
    return abs(a*b) // gcd(a,b)

print(lcm(18, 48))
<jupyter_output>
144
<jupyter_text>
6. Write a Python function to check if a number is prime or not.
<jupyter_code>
def is_prime(n):
    if n <= 1:
        return