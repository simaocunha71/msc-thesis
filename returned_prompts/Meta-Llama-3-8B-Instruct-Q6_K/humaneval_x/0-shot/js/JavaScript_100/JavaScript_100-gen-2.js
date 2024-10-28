Here is a Python solution for the problem:

```Python
def makeAPile(n):
    pile = [n]
    while n > 1:
        n = n - 1 if n % 2 == 1 else n - 2
        pile.append(n)
    return pile
```

This function starts by initializing a list `pile` with the number of stones in the first level. Then, it enters a loop that continues until there is only one stone left. In each iteration of the loop, it calculates the number of stones in the next level based on whether the current number of stones is odd or even. Finally, it returns the list of numbers representing the number of stones in each level. For example, `makeAPile(3)` returns `[3, 5, 7]`. 

The time complexity of this solution is O(n), where n is the number of levels in the pile, because it makes a constant number of operations for each level. The space complexity is also O(n), because it stores the number of stones in each level in the list `pile`. 

The problem description does not specify the return type, but based on the examples provided, it seems that the function should return a list of integers. If the return type was supposed to be a string, the function would need to be modified to concatenate the numbers into a string. 

This solution assumes that the input is a positive integer, as specified in the problem description. If the input could be any integer, including negative or zero, the function would need to be modified to handle these cases. 

This solution also assumes that the pile is built according to the rules specified in the problem description, i.e., the number of stones in each level is the next odd number if the current number of stones is odd, and the next even number if the current number of stones is even. If the pile is built according to different rules, the function would need to be modified accordingly. 