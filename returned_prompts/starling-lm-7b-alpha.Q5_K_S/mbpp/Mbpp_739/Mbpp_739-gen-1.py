```
def find_Index(n):
    i = 1
    while len(str(i*(i+1)//2)) < n:
        i+=1
    return i
```

Explanation:
The triangular numbers are the numbers of the form i(i+1)/2, where i is a non-negative integer. The smallest triangular number with n digits is the smallest i such that the length of the string representation of i(i+1)/2 is exactly equal to n. The function find_Index(n) computes the smallest i that satisfies this condition.

For example, when n = 2, the smallest triangular number with 2 digits is 4. This can be computed by checking each positive integer i from 1 to infinity until the length of the string representation of i(i+1)/2 is exactly equal to 2. The function find_Index(n) returns the value of i that satisfies this condition.

The function find_Index(n) uses a while loop to increment the value of i until the length of the string representation of i(i+1)/2 is exactly equal to n. The condition len(str(i*(i+1)//2)) < n checks if the length of the string representation of i(i+1)/2 is less than n. If this condition is true, the while loop continues to increment the value of i. Once the condition is no longer true, the while loop stops and the function returns the value of i.

The function find_Index(n) can be called with any non-negative integer n to find the index of the smallest triangular number with n digits.

The assert statement at the beginning of the code checks if the function find_Index(n) correctly computes the index of the smallest triangular number with n digits for the given input n = 2. The assert statement is a way to check if a condition is true and raises an error if the condition is false. In this case, the assert statement checks if find_Index(n) correctly returns 4 for the input n = 2, and raises an error if the function does not return the correct result.

In summary, the function find_Index(n) computes the index of the smallest triangular number with n digits. The assert statement at the beginning of the