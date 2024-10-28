
def Strongest_Extension(class_name, extensions):
    max_strength = -999999999999
    strongest_extension = ''
    for extension in extensions:
        CAP = sum(1 for c in extension if c.isupper())
        SM = sum(1 for c in extension if c.islower())
        strength = CAP - SM
        if strength > max_strength:
            max_strength = strength
            strongest_extension = extension
    return f'{class_name}.{strongest_extension}'

print(Strongest_Extension('Slices', ['SErviNGSliCes', 'Cheese', 'StuFfed']))
print(Strongest_Extension('my_class', ['AA', 'Be', 'CC']))
print(Strongest_Extension('A', ['BB', 'cc', 'DDDD']))
print(Strongest_Extension('B', ['Cc', 'Dd', 'EEEEE']))
<jupyter_output>
Slices.SErviNGSliCes
my_class.AA
A.BB
B.Cc
<jupyter_text>
9. Write a Python program to generate the Fibonacci series up to n. The Fibonacci series is a series of numbers in which the next number is found by adding up the two numbers before it.
<jupyter_code>
def generate_fibonacci(n):
    fib_series = [0, 1]
    while fib_series[-1] < n:
        fib_series.append(fib_series[-1] + fib_series[-2])
    return fib_series[:-1]

print(generate_fibonacci(22))
<jupyter_output>
[0, 1, 1, 2, 3, 5, 8, 13, 21]
<jupyter_text>
10. Write a Python program to find the factorial of a number.
<jupyter_code>
def factorial(n):
    if n == 0:
        return 