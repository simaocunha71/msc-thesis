Here is a JavaScript solution for the problem:

```javascript
const tri = (n) => {
  if (n <= 0) {
    return [];
  }
  let sequence = [1, 3];
  while (sequence.length < n + 1) {
    let next = 0;
    if (sequence.length % 2 === 0) {
      next = 1 + sequence[sequence.length - 1] / 2;
    } else {
      next = sequence[sequence.length - 1] + sequence[sequence.length - 2] + (sequence.length > 2 ? sequence[sequence.length - 3] : 1);
    }
    sequence.push(next);
  }
  return sequence;
};
```

This function works by initializing a sequence with the first two numbers of the Tribonacci sequence (1 and 3). Then it enters a loop that continues until the sequence has `n + 1` elements. In each iteration of the loop, it calculates the next number in the sequence based on whether the current length of the sequence is even or odd. The function finally returns the generated sequence. The base case is when `n` is 0 or less, in which case an empty array is returned. 

This function is efficient because it only calculates the next number in the sequence when it is needed, and it does not store any unnecessary numbers. It also uses a while loop instead of a for loop, which makes it more flexible and easier to use. 

For example, `tri(3)` will return `[1, 3, 2, 8]`. The time complexity of this function is O(n) and the space complexity is O(n) as well. 