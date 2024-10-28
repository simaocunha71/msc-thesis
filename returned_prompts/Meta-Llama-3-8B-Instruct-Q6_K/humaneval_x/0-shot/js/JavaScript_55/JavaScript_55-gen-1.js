```
  if (n <= 1) {
    return n;
  }
  let a = 0;
  let b = 1;
  for (let i = 2; i <= n; i++) {
    [a, b] = [b, a + b];
  }
  return b;
}
```
Explanation:
The Fibonacci sequence is defined as a series of numbers where each number is the sum of the two preceding ones, usually starting with 0 and 1. This function uses a simple iterative approach to calculate the n-th Fibonacci number.

It first checks if the input `n` is less than or equal to 1, in which case it returns `n` as the Fibonacci sequence starts with 0 and 1.

Then, it initializes two variables `a` and `b` to 0 and 1, which are the first two numbers in the Fibonacci sequence.

The function then uses a for loop to iterate from 2 to `n`. In each iteration, it updates `a` and `b` to be the sum of the previous two numbers in the sequence. This is done using the array destructuring syntax `[a, b] = [b, a + b]`, which swaps the values of `a` and `b` and updates `a` to be the sum of the previous `b` and `a`.

Finally, the function returns `b`, which is the n-th Fibonacci number.

This function has a time complexity of O(n) and a space complexity of O(1), making it efficient for calculating Fibonacci numbers.