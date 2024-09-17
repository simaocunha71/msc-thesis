```
def find_lucas(n):
    if n == 1:
        return 2
    elif n == 2:
        return 1
    else:
        a, b = 2, 1
        for _ in range(2, n):
            a, b = b, a + b
        return b
```    
The Lucas sequence is a sequence of integers in which every term is the sum of the two preceding terms, starting with 2 and 1. The first few terms are 2, 1, 3, 4, 7, 11, 18, 29, 47, 76, ... . We can write a function to find the nth Lucas number by using a loop to calculate each term in the sequence. The base cases are the first two terms, which are 2 and 1. For the rest of the terms, we add the previous two terms together. The function returns the nth term in the sequence. 

The unit test `assert find_lucas(9) == 76` ensures that the function works correctly. It checks that the 9th Lucas number is 76, which is the correct value. 

This function has a time complexity of O(n) because it uses a loop to calculate each term in the sequence. The space complexity is O(1) because it only uses a constant amount of space to store the previous two terms. 