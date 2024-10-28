  if (n < 0) {
    throw new Error('Input should be a non-negative integer');
  }

  if (n < 3) {
    return n === 2 ? 1 : 0;
  }

  let a = 0, b = 0, c = 1, d;

  for (let i = 3; i <= n; i++) {
    d = a + b + c;
    a = b;
    b = c;
    c = d;
  }

  return d;
};
console.log(fibfib(1));
console.log(fibfib(5));
console.log(fibfib(8));
```

This problem can be solved using a dynamic programming approach. We define an array of size n + 1 and fill it with zeros. The base cases are then initialized at the appropriate indices of the array. Finally, we loop through the array from the 4th element to the nth element and update each element by adding the previous three elements. The nth element of the array is then returned as the nth FibFib number.

This solution is efficient as it only requires a single pass through the array and has a time complexity of O(n). The space complexity is also O(n) due to the array.

Note: The FibFib sequence defined in the problem is equivalent to the Fibonacci sequence if we replace each FibFib(n) with Fib(n), where Fib(n) is the n-th number in the Fibonacci sequence (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...).

The Fibonacci sequence defined in the problem is different from the Fibonacci sequence in the standard mathematical definition (0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...). The standard Fibonacci sequence is defined by the recurrence relation Fib(n) = Fib(n-1) + Fib(n-2), with initial conditions Fib(0) = 0 and Fib(1) = 1. The