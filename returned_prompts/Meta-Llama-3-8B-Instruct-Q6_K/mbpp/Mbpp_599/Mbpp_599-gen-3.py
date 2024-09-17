```
def sum_average(n):
    sum = n*(n+1)//2
    average = sum/n
    return sum, average
```
This function calculates the sum of the first n natural numbers using the formula n*(n+1)//2 and then calculates the average by dividing the sum by n. It returns both the sum and the average. The unit test `assert sum_average(10)==(55, 5.5)` confirms that the function works correctly. 
The function works by first calculating the sum of the first n natural numbers, which is given by the formula n*(n+1)//2. This is because the sum of the first n natural numbers is equal to the sum of the first n-1 natural numbers plus n, so it can be calculated recursively. 

The average is then calculated by dividing the sum by n. This is because the average of a set of numbers is equal to the sum of the numbers divided by the number of numbers in the set. 

The function returns both the sum and the average as a tuple. This is because the problem statement asks for both the sum and the average to be returned, and returning them as a tuple is a convenient way to do this. 

The function works correctly for any positive integer n, and it does not have any limitations or edge cases that would cause it to fail. It is a simple and efficient solution to the problem. 

The unit test `assert sum_average(10)==(55, 5.5)` confirms that the function works correctly. This test checks that the sum and average of the first 10 natural numbers are both 55 and 5.5, respectively. If the function is working correctly, this test should pass. If the function is not working correctly, this test will fail. 

In summary, this function calculates the sum and average of the first n natural numbers using the formulas n*(n+1)//2 and sum/n, respectively. It returns both the sum and the average as a tuple, and it works correctly for any positive integer n. The unit test `assert sum_average(10)==(55, 5.5)` confirms that the function works correctly. 