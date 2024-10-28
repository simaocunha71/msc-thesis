To solve this problem, we need to follow these steps:

1. Round each element in the list to the upper int (Ceiling).
2. Square each element in the rounded list.
3. Sum all the squared elements in the rounded list.
4. Return the sum.

Here's the detailed step-by-step solution in Python:

Step 1: Round each element in the list to the upper int (Ceiling).
To round each element to the upper int (Ceiling), we can use the ceil() function from the math module in Python. Here's how to do it:

rounded_lst = [math.ceil(num) for num in lst]

Step 2: Square each element in the rounded list.
To square each element in the rounded list, we can use a list comprehension with the ** operator. Here's how to do it:

squared_lst = [num ** 2 for num in rounded_lst]

Step 3: Sum all the squared elements in the rounded list.
To sum all the squared elements in the rounded list, we can use the sum() function. Here's how to do it:

sum_squares = sum(squared_lst)

Step 4: Return the sum.
Finally, we can return the sum_squares variable, which will be the sum of squared numbers in the given list. Here's how to do it:

return sum_squares

Here's the complete solution in Python:

import math

def sumSquares(lst):
    rounded_lst = [math.ceil(num) for num in lst]
    squared_lst = [num ** 2 for num in rounded_lst]
    sum_squares = sum(squared_lst)
    return sum_squares

You can use this function to calculate the sum of squared numbers in any given list of numbers.

*/

// JavaScript Solution

function sumSquares(lst){
    const roundedList = lst.map(num => Math.ceil(num));
    const squaredList = roundedList.map(num => num * num);
    return squaredList.reduce((sum