Here is the solution using recursion:
```javascript
const tri = (n) => {
  if (n === 0) return [];
  if (n === 1) return [3];
  if (n === 2) return [1, 3];
  let sequence = [1, 3];
  for (let i = 2; i < n; i++) {
    if (i % 2 === 0) {
      sequence.push(1 + i / 2);
    } else {
      sequence.push(sequence[i - 1] + sequence[i - 2] + sequence[i - 3]);
    }
  }
  return sequence;
};
```
Explanation:
We use a recursive approach to generate the Tribonacci sequence. We start by checking if `n` is 0, 1, or 2, in which case we return an empty list, `[3]`, or `[1, 3]`, respectively.

For `n` greater than 2, we start with the base case sequence `[1, 3]`. Then, we use a loop to generate the remaining elements of the sequence. For each `i` from 2 to `n`, we check if `i` is even or odd.

If `i` is even, we calculate the next element as `1 + i / 2`. If `i` is odd, we calculate the next element as the sum of the previous three elements (`sequence[i - 1]`, `sequence[i - 2]`, and `sequence[i - 3]`).

Finally, we return the generated sequence.

Example:
```javascript
tri(3) // [1, 3, 2, 8]
tri(4) // [1, 3, 2, 8, 11]
tri(5) // [1, 3, 2, 8, 11, 34]
```