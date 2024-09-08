
def square_Sum(n):
    sum = 0
    num = 1
    for i in range(n):
        sum += num * num
        num += 2
    return sum

print(square_Sum(2)) # 10

"""
The function works by first initializing a sum to 0 and a num to 1. The num is initialized to 1 because the first odd number is 1. 
Then a for loop is used to iterate n times. In each iteration, the square of num (which is currently an odd number) is added to the sum and num is incremented by 2 to get the next odd number.
Finally, the sum is returned.
"""
<jupyter_output>
10
<jupyter_text>
Q2: Write a python function that takes a list of integers and returns a new list with the squares of the elements of the original list.
<jupyter_code>
def square_list(lst):
    return [i ** 2 for i in lst]

print(square_list([1, 2, 3, 4])) # [1, 4, 9, 16]
<jupyter_output>
[1, 4, 9, 16]
<jupyter_text>
Q3: Write a python function that takes an integer n and returns the sum of the squares of the first n natural numbers.
<jupyter_code>
def square_sum(n):
    return sum([i ** 2 for i in range(1, n+1)])

print(square_sum(4)) # 30
<jupyter_output>
30
<jupyter_text>
Q4: Write a python function that takes a list of integers and returns the sum of the squares of the even numbers in the list.
<jupyter_code>
def square_sum_even(lst):
    return sum([i ** 2 for i in lst if i % 2 == 0])

print(square_sum_even([1, 2, 3, 4])) # 20
<jupyter_output>
20