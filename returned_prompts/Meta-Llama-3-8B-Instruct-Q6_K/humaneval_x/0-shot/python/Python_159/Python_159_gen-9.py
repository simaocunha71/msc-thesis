
Here is the Python code for the problem:

```
def eat(number, need, remaining):
    eaten = number + (remaining if remaining >= need - number else need - number)
    left = remaining - (eaten - number)
    return [eaten, left]
```

Explanation:

1. First, we calculate the total number of carrots eaten by adding the number of carrots already eaten (`number`) with the number of carrots needed minus the number of carrots already eaten (`need - number`). If there are not enough remaining carrots, we will eat all remaining carrots.

2. Next, we calculate the number of carrots left by subtracting the difference between the total number of carrots eaten and the number of carrots already eaten from the remaining carrots.

3. Finally, we return a list containing the total number of carrots eaten and the number of carrots left. If there are not enough remaining carrots, the number of carrots left will be 0.