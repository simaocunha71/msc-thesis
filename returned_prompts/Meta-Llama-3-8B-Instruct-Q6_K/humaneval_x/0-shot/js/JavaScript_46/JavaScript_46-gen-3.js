Here is a Python solution for the problem:

```
def fib4(n):
    if n <= 1:
        return 0
    if n == 2:
        return 2
    fib4_values = [0, 0, 2, 0]
    for i in range(4, n+1):
        fib4_values.append(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4])
    return fib4_values[n]
```

In this solution, we first handle the base cases where n is less than or equal to 1 or equal to 2. Then we create a list fib4_values to store the values of the fib4 sequence. We iterate from 4 to n and append the sum of the last 4 values in the list to the list. Finally, we return the n-th element of the list.

This solution has a time complexity of O(n) because we are iterating from 4 to n. The space complexity is also O(n) because we are storing the values of the fib4 sequence in a list.

You can test the function with the following code:

```
print(fib4(5))  # Output: 4
print(fib4(6))  # Output: 8
print(fib4(7))  # Output: 14
```


Here is a JavaScript solution for the problem:

```
function fib4(n) {
    if (n <= 1) {
        return 0;
    }
    if (n == 2) {
        return 2;
    }
    let fib4_values = [0, 0, 2, 0];
    for (let i = 4; i <= n; i++) {
        fib4_values.push(fib4_values[i-1] + fib4_values[i-2] + fib4_values[i-3] + fib4_values[i-4]);
    }
    return fib4_values[n];
}
```

You can test the function with the following code:

```
console.log(fib4(5));  // Output: 4
console.log(fib4(6));  // Output: 8
console.log(fib4(7));  // Output: 14
```


This JavaScript solution is similar to the Python solution. It first handles the base cases where n is less than or equal to 1 or