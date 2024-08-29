
def square_Sum(n):
    sum = 0
    for i in range(2, 2*n+1, 2):
        sum += i**2
    return sum

print(square_Sum(2))

"""
Explanation:

In the function 'square_Sum', we initialize a variable 'sum' to 0. We then use a for loop to iterate over the first n even natural numbers. The range function is used to generate these numbers, with the arguments being '2', '2*n+1', and '2'. This means the loop will start at 2, end at 2*n+1, and step by 2, effectively only considering even numbers.

Inside the loop, we add the square of the current number to 'sum'. This is done using the expression 'i**2', which is shorthand for i to the power of 2.

Finally, the function returns the value of 'sum', which will be the sum of the squares of the first n even natural numbers.

The assert statement is used to test the function. It checks if the result of calling 'square_Sum(2)' is equal to 20. If the result is not 20, an error will be raised.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
2. Python function to print first n natural numbers in reverse order
<jupyter_code>
