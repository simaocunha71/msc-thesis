```
def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(math.factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result
```
This function uses a for loop to iterate over the range from 1 to n. For each iteration, it checks if the current number i is even (i % 2 == 0). If it is, it calculates the factorial of i using the math.factorial function and appends it to the result list. If i is odd, it calculates the sum of numbers from 1 to i using the sum function and range function, and appends it to the result list. Finally, it returns the result list. 

For example, when n is 5, the function will return [1, 2, 6, 24, 15], which is the expected output. 

Please note that you need to import the math module at the beginning of your code to use the factorial function. 

Here is the complete code:
```
import math

def f(n):
    result = []
    for i in range(1, n+1):
        if i % 2 == 0:
            result.append(math.factorial(i))
        else:
            result.append(sum(range(1, i+1)))
    return result

print(f(5))  # Output: [1, 2, 6, 24, 15]
```  