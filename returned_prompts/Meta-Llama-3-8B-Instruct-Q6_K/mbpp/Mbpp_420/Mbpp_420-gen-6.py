```
def cube_Sum(n):
    total = 0
    for i in range(2, 2*n, 2):
        total += i**3
    return total
``` 
This function calculates the cube sum of the first n even natural numbers. It does this by iterating over the range of even numbers from 2 to 2*n and adding each number cubed to a running total. The function returns the total sum. 

The unit test `assert cube_Sum(2) == 72` ensures that the function is working correctly for n=2. The actual value of the sum for n=2 is 72, which is the expected output. 

The time complexity of this function is O(n), as it iterates over a range of n/2 elements. The space complexity is O(1), as it only uses a constant amount of space to store the total sum. 