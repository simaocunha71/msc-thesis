The problem can be solved by using two nested loops to generate all n-digit numbers
and then checking if the number starts or ends with 1. However, this approach is not
efficient for large values of n.

A more efficient approach is to use the concept of combinatorics. The number of n-digit
numbers that start with 1 is 9^(n-1), and the number of n-digit numbers that end with 1
is 10^(n-1) - 9^(n-1). Therefore, the total count is the sum of these two values.

Here is the code:

```javascript
const startsOneEnds = (n) => {
    if (n < 1) {
        return 0;
    }
    return (9 ** (n - 1)) + (10 ** (n - 1) - 9 ** (n - 1));
};
```

This code first checks if the input n is less than 1, and if so, returns 0. Otherwise,
it calculates the count of n-digit numbers that start with 1 using the formula 9^(n-1),
and then calculates the count of n-digit numbers that end with 1 using the formula
10^(n-1) - 9^(n-1). Finally, it returns the sum of these two values.

This code has a time complexity of O(1), making it efficient for large values of n.