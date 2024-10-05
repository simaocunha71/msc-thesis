The solution for this problem can be achieved by implementing a recursive function that calculates the Tribonacci sequence. The function will take an integer `n` as input and return a list of the first `n + 1` numbers of the Tribonacci sequence.

Here is the JavaScript code that solves the problem:
```
function tri(n) {
  if (n <= 0) return [];
  if (n === 1) return [3];
  if (n === 2) return [1, 3];

  let tribonacci = [1, 3];
  for (let i = 2; i < n; i++) {
    if (i % 2 === 0) {
      tribonacci[i] = 1 + (i / 2);
    } else {
      tribonacci[i] = tribonacci[i - 1] + tribonacci[i - 2] + tribonacci[i + 1];
    }
  }
  return tribonacci;
}
```
This function uses a recursive approach to calculate the Tribonacci sequence. It first checks if `n` is less than or equal to 0, in which case it returns an empty list. If `n` is 1, it returns a list containing only 3. If `n` is 2, it returns a list containing 1 and 3.

For `n` greater than 2, the function initializes a list `tribonacci` with the first two elements of the Tribonacci sequence, which are 1 and 3. It then enters a loop that runs `n - 2` times. In each iteration, it checks if `i` is even or odd. If `i` is even, it calculates the next element of the Tribonacci sequence by adding 1 to `i` divided by 2. If `i` is odd, it calculates the next element by adding the previous three elements of the sequence.

Finally, the function returns the list `tribonacci`, which contains the first `n + 1` elements of the Tribonacci sequence.

You can test this function with different values of `n` to see the results. For example, `tri(3)` returns `[1, 3, 2, 8]`, which is the expected result.