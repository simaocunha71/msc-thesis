The Fibonacci sequence is a series of numbers where the next number is found by adding up the two numbers before it. The sequence starts 0, 1, 1, 2, 3, 5, 8, 13, 21, 34, ...

In the sequence above, 21 is found by adding 8 and 13, 34 is found by adding 21 and 13, and so on.

The problem is asking to return the n-th Fibonacci number. The n-th Fibonacci number is the number in the sequence at position n.

For example, the first Fibonacci number is 1, the second Fibonacci number is 1, the third Fibonacci number is 2, the fourth Fibonacci number is 3, and so on.

Here's the solution in JavaScript:

```
const fib = (n) => {
  if (n <= 1) {
    return n;
  }
  let a = 0;
  let b = 1;
  for (let i = 2; i <= n; i++) {
    let temp = a + b;
    a = b;
    b = temp;
  }
  return b;
}
```

In this solution, we first check if n is less than or equal to 1. If it is, we return n because the first and second Fibonacci numbers are both 1.

If n is greater than 1, we initialize two variables a and b to 0 and 1, respectively. Then, we iterate from 2 to n using a for loop. In each iteration, we calculate the next Fibonacci number by adding a and b and store it in a temporary variable temp. Then, we update a to be b and b to be temp. Finally, we return b, which is the n-th Fibonacci number.