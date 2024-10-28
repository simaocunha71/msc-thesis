  let sequence = '';
  for(let i = 0; i <= n; i++) {
    sequence += i + ' ';
  }
  return sequence.trim();
}

console.log(stringSequence(0)) // '0'
console.log(stringSequence(5)) // '0 1 2 3 4 5'
```

This function works by initializing an empty string `sequence`. It then uses a `for` loop to iterate from `0` to `n` (inclusive). In each iteration, it appends the current number `i` followed by a space to `sequence`. Finally, it uses `.trim()` to remove the trailing space before returning `sequence`.

This function will work for any valid positive integer `n`. For `n = 0`, it will return `'0'`. For `n > 0`, it will return a string of space-delimited numbers starting from `0` up to `n` inclusive.

Here is a simple test:

```javascript
console.log(stringSequence(0)) // '0'
console.log(stringSequence(5)) // '0 1 2 3 4 5'
```
This will output `'0'` and `'0 1 2 3 4 5'` respectively.

The time complexity of this function is O(n), as it iterates from `0` to `n`. The space complexity is also O(n), as it stores the string sequence in memory.
*/

const stringSequence = (n) => {
  let sequence = '';
  for(let i = 0; i <= n; i++) {
    sequence += i + ' ';
  }
  return sequence.trim();
}

console.log(stringSequence(0)) // '0'
console.log(stringSequence(5)) // '0 1 2 3 4 5'
```


## Explanation:
The function `stringSequence` takes an input `n` and returns a string of numbers from 0 to `n` separated by spaces.

The function is initialized with an empty string `sequence`. It then uses a `for` loop to iterate over