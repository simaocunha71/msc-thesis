Here is a function to efficiently compute the n-th element of the fibfib number sequence:
```
const fibfib = (n) => {
  if (n <= 1) return 0;
  if (n === 2) return 1;
  let a = 0, b = 0, c = 1;
  for (let i = 3; i <= n; i++) {
    let temp = a + b + c;
    a = b;
    b = c;
    c = temp;
  }
  return c;
};
```
Here's an explanation of the code:

1. We handle the base cases `n <= 1` and `n === 2` separately, as they have special values.
2. We initialize three variables `a`, `b`, and `c` to keep track of the previous three elements of the sequence.
3. We use a loop to compute the `n`-th element. In each iteration, we calculate the next element as the sum of the previous three elements (`a`, `b`, and `c`).
4. We update the values of `a`, `b`, and `c` for the next iteration.
5. Finally, we return the `n`-th element, which is stored in `c`.

This function has a time complexity of O(n), making it efficient for large values of `n`. You can test it with the examples you provided:
```
console.log(fibfib(1)); // 0
console.log(fibfib(5)); // 4
console.log(fibfib(8)); // 24
```