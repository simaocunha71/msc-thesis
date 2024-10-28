To solve this problem we can use dynamic programming to store the FibFib numbers for all values up to n.

First, we'll initialize an array called `fibfib` with the first three FibFib numbers. Then, we'll fill in the rest of the array using the FibFib recursive formula. Finally, we'll return the nth FibFib number from the `fibfib` array.

Here's the step-by-step code:

1. Initialize an array called `fibfib` with the first three FibFib numbers.
```javascript
const fibfib = [0, 0, 1];
```
2. Use a for loop to fill in the rest of the `fibfib` array using the FibFib recursive formula.
```javascript
for (let i = 3; i <= n; i++) {
  fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
}
```
3. Return the nth FibFib number from the `fibfib` array.
```javascript
return fibfib[n];
```
4. Putting it all together:
```javascript
const fibfib = (n) => {
  const fibfib = [0, 0, 1];

  for (let i = 3; i <= n; i++) {
    fibfib[i] = fibfib[i - 1] + fibfib[i - 2] + fibfib[i - 3];
  }

  return fibfib[n];
};
```

Now you can use the `fibfib` function to compute the nth FibFib number. For example, `fibfib(1)` returns `0`, `fibfib(5)` returns `4`, and `fibfib(8)` returns `24`.

*/

const fibfib = (n) => {
  const fibfib = [0, 0, 1];

  for (let i = 3;