```javascript
function fib(n) {
  if (n <= 1) {
    return n;
  }
  let a = 0, b = 1, result = 0;
  for (let i = 2; i <= n; i++) {
    result = a + b;
    a = b;
    b = result;
  }
  return result;
}

console.log(fib(10)); // 55
console.log(fib(1)); // 1
console.log(fib(8)); // 21
```


The above code defines a function `fib` that calculates the `n-th` Fibonacci number. The Fibonacci sequence is a series of numbers in which each number is the sum of the two preceding ones, usually starting with 0 and 1.

In the function, we use a for loop to iterate from 2 to `n`, and in each iteration, we calculate the next Fibonacci number as the sum of the previous two numbers, `a` and `b`. We then update `a` and `b` to be the last two numbers in the sequence.

The function returns the `n-th` Fibonacci number. In the console logs, we call the function with arguments 10, 1, and 8, and print the results, which are 55, 1, and 21, respectively. These values match the expected results for the Fibonacci sequence.