  if (n <= 2) {
    return 1;
  }
  let prev = 1;
  let curr = 1;
  for (let i = 3; i <= n; i++) {
    let temp = curr;
    curr += prev;
    prev = temp;
  }
  return curr;
};

module.exports = fib;

// console.log(fib(10));
// console.log(fib(1));
// console.log(fib(8));

// Output:
// 55
// 1
// 21
```

The function `fib(n)` will return the nth Fibonacci number. It uses a simple for loop to iterate from 3 to `n` (inclusive), at each iteration, it adds `prev` and `curr` to calculate the next Fibonacci number and updates `curr` and `prev`. When the loop finishes, it returns `curr` as the nth Fibonacci number. If `n` is 1 or 2, the function will return 1 as the Fibonacci sequence starts with 1 and 1.

This function has a time complexity of O(n), and a space complexity of O(1), which means it uses a constant amount of memory to store variables regardless of the input size.

Note: This solution assumes that the input `n` is a non-negative integer. If the input can be a floating-point number or a negative number, you need to add additional error checking code.

## Resources

- [Fibonacci Sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)
- [Dynamic Programming](https://en.wikipedia.org/wiki/Dynamic_programming)
- [Big O notation](https://en.wikipedia.org/wiki/Big_O_notation)
- [Recursion vs Iteration](https://www.geeksforgeeks.org/recursion-vs-iteration/)
- [Memoization](https://en.wikipedia.org/wiki/Memoization)
- [Fibonacci Sequence with Memoization](