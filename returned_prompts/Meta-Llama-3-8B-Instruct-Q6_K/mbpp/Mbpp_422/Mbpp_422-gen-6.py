```
def find_Average_Of_Cube(n):
    total = 0
    for i in range(1, n + 1):
        total += i ** 3
    return total / n
```


This function calculates the sum of cubes of first n natural numbers and then divides it by n to find the average. It uses a for loop to iterate over the range of numbers from 1 to n, cubes each number and adds it to the total. Finally, it returns the total divided by n. The unit test `assert find_Average_Of_Cube(2) == 4.5` helps to verify the correctness of the function. 





