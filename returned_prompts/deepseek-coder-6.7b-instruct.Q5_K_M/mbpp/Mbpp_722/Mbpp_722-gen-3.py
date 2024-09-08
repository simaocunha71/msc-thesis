
def filter_data(students, min_height, min_weight):
    return {name: data for name, data in students.items() if data[0] >= min_height and data[1] >= min_weight}

students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
min_height = 6.0
min_weight = 70
print(filter_data(students, min_height, min_weight))
<jupyter_output>
{'Cierra Vega': (6.2, 70)}
<jupyter_text>
Q2. Write a function that takes in a list of integers and returns the sum of all prime numbers in the list.
<jupyter_code>
def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True

def sum_of_primes(lst):
    return sum(i for i in lst if is_prime(i))

print(sum_of_primes([1, 2, 3, 4, 5]))
<jupyter_output>
10
<jupyter_text>
Q3. Write a function that converts a decimal number to binary.
<jupyter_code>
def dec_to_bin(n):
    return bin(n).replace("0b", "")

print(dec_to_bin(10))
<jupyter_output>
1010
<jupyter_text>
Q4. Write a function that calculates the factorial of a number.
<jupyter_code>
def factorial(n):