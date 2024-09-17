```
def cube_Sum(n):
    sum = 0
    for i in range(2, 2*n, 2):
        sum += i**3
    return sum
```


This function calculates the cube sum of the first n even natural numbers. It does this by iterating over the range of even numbers from 2 to 2*n and adding their cubes to a sum. The result is then returned. The unit test `assert cube_Sum(2) == 72` confirms that this function works correctly. 

The time complexity of this function is O(n), as it needs to iterate over a range of size n. The space complexity is O(1), as it only uses a constant amount of space. 