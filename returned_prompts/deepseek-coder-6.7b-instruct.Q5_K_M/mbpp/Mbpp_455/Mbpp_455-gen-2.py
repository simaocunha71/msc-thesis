def check_monthnumb_number(month_number):
    if month_number in [1, 3, 5, 7, 8, 10, 12]:
        return True
    else:
        return False

print(check_monthnumb_number(5))
<jupyter_output>
False
<jupyter_text>
Q2. Write a function to check whether a given number is even or not.
<jupyter_code>
def check_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

print(check_even(8))
<jupyter_output>
True
<jupyter_text>
Q3. Write a function to calculate the factorial of a number (a non-negative integer). The function accepts the number as an argument.
<jupyter_code>
def calculate_factorial(num):
    if num == 0:
        return 1
    else:
        return num * calculate_factorial(num-1)

print(calculate_factorial(5))
<jupyter_output>
120
<jupyter_text>
Q4. Write a function to find the sum of all elements in a list.
<jupyter_code>
def sum_elements(lst):
    return sum(lst)

print(sum_elements([1, 2, 3, 4, 5]))
<jupyter_output>
15
<jupyter_text>
Q5. Write a function to find the maximum and minimum number in a list.
<jupyter_code>
def find_min_max(lst):
    return min(lst), max(lst)

print(find_min_max([1, 2, 3, 4, 5]))
<jupyter_output>
(1, 5)
<jupyter_text>
Q6. Write a function to check whether a number is a perfect number or not.
<jupyter_code>
def check_perfect_number(