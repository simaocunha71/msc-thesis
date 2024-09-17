```
def find_Average_Of_Cube(n):
    total = sum(i**3 for i in range(1, n+1))
    return total / n
```
This function calculates the sum of cubes of first n natural numbers and then divides the sum by n to find the average. 

The unit test `assert find_Average_Of_Cube(2) == 4.5` ensures that the function is working correctly. The average of the cubes of the first 2 natural numbers is indeed 4.5. 

Note that this function assumes that n is a positive integer. If n can be negative or non-integer, you may want to add error checking code. 