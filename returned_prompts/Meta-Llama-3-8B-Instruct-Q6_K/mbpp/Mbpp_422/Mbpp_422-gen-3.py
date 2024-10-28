```
def find_Average_Of_Cube(n):
    sum_of_cubes = sum(i**3 for i in range(1, n+1))
    return sum_of_cubes / n
```
This function calculates the sum of cubes of first n natural numbers and then divides it by n to find the average. The unit test `assert find_Average_Of_Cube(2) == 4.5` helps to clarify the expected output of the function. 

In this function, the `sum` function is used to calculate the sum of cubes of first n natural numbers. The `range` function is used to generate a sequence of numbers from 1 to n (inclusive). The `**` operator is used to cube each number in the sequence. The `sum` function returns the sum of all the numbers in the sequence. The average is then calculated by dividing the sum by n. 