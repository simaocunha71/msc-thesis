```
def find_Average_Of_Cube(n):
    sum = 0
    for i in range(1, n+1):
        sum += i**3
    return sum / n
```


This function calculates the average of the cubes of the first n natural numbers. It does this by summing the cubes of the numbers from 1 to n and then dividing by n. The unit test `assert find_Average_Of_Cube(2) == 4.5` checks that the function returns the correct result for n=2. 

For example, the average of the cubes of the first 2 natural numbers is (1^3 + 2^3) / 2 = 9 / 2 = 4.5. The function correctly returns this result. 