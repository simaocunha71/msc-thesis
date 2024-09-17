```
def square_Sum(n):
    return sum([i**2 for i in range(1, 2*n, 2)])
``` 
Explanation:
The problem asks to find the sum of the squares of the first n odd natural numbers. We can use list comprehension to generate the odd numbers and then square each number. We use range function to generate the numbers, and 2*n is used as the stop point because we want to include n in our sequence. The step size is 2 because we are only interested in odd numbers. Finally, we use the sum function to add up all the squares. 

The unit test `assert square_Sum(2) == 10` helps to clarify the problem by showing that the function should return 10 when n is 2. This means that the function should sum the squares of the first 2 odd natural numbers, which are 1 and 3. The square of 1 is 1 and the square of 3 is 9, so the sum is 1 + 9 = 10. 





The unit test `assert square_Sum(2) == 10` helps to clarify the problem by showing that the function should return 10 when n is 2. This means that the function should sum the squares of the first 2 odd natural numbers, which are 1 and 3. The square of 1 is 1 and the square of 3 is 9, so the sum is 1 + 9 = 10. 





This solution uses list comprehension to generate the odd numbers, squares each number, and then sums them up. It is concise and efficient, and passes the given unit test.