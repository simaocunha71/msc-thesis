```javascript
const fib = (n) => {
  if (n <= 1) {
    return n;
  }
  let a = 1;
  let b = 1;
  for (let i = 2; i < n; i++) {
    const sum = a + b;
    a = b;
    b = sum;
  }
  return b;
};
```


Explanation:
The function `fib` takes an integer `n` as input and returns the `n-th` Fibonacci number. The Fibonacci sequence is defined as: `F(0) = 0`, `F(1) = 1`, `F(n) = F(n-1) + F(n-2)` for `n > 1`. 

In the function, we first check if `n` is less than or equal to 1. If so, we return `n` because the first two Fibonacci numbers are 0 and 1.

For `n > 1`, we initialize two variables `a` and `b` to 1, which are the first two Fibonacci numbers. We then use a for loop to calculate the `n-th` Fibonacci number. In each iteration, we calculate the sum of `a` and `b` and update `a` and `b` to the sum and the previous value of `a` respectively. After the loop, `b` will be the `n-th` Fibonacci number, which we return. 

This function has a time complexity of O(n) because it uses a single loop to calculate the `n-th` Fibonacci number. The space complexity is O(1) because it only uses a constant amount of space to store the variables `a`, `b` and `i`. 

You can test this function with different inputs, such as `fib(10)`, `fib(1)`, `fib(8)`, to verify that it returns the correct Fibonacci numbers. 