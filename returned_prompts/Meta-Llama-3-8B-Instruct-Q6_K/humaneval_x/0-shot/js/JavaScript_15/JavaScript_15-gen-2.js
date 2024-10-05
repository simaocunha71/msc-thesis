```
const stringSequence = (n) => {
  let result = '';
  for (let i = 0; i <= n; i++) {
    result += i + ' ';
  }
  return result.trim();
};
```


Explanation:
1. We initialize an empty string `result` to store the sequence of numbers.
2. We use a `for` loop to iterate from 0 to `n` (inclusive).
3. Inside the loop, we concatenate the current number `i` to the `result` string followed by a space `' '`.
4. After the loop, we use the `trim()` method to remove the trailing space at the end of the `result` string.
5. We return the `result` string.

Example usage:
```
console.log(stringSequence(0)); // Output: "0"
console.log(stringSequence(5)); // Output: "0 1 2 3 4 5"
```


Note: The `trim()` method is used to remove the trailing space at the end of the `result` string. This is necessary because the last iteration of the loop appends a space to the `result` string, and we don't want this extra space to be part of the final output.