```
const getOddCollatz = (n) => {
  let result = [];
  let num = n;
  while (num !== 1) {
    if (num % 2 !== 0) {
      result.push(num);
      num = num * 3 + 1;
    } else {
      num = Math.floor(num / 2);
    }
  }
  result.push(1);
  return result.sort((a, b) => a - b);
};
```


Explanation:

1. Initialize an empty array `result` to store the odd numbers in the Collatz sequence.
2. Set `num` to the input `n`.
3. Loop until `num` is 1.
   - If `num` is odd, push it to the `result` array and update `num` to the next value in the sequence (which is `num * 3 + 1`).
   - If `num` is even, update `num` to the next value in the sequence (which is `Math.floor(num / 2)`).
4. After the loop, push 1 to the `result` array (since the sequence always ends with 1).
5. Return the `result` array sorted in increasing order using the `sort()` method.

Example:
```
getOddCollatz(5) // [1, 5]
getOddCollatz(12) // [1, 3, 10]
```



Note: This solution assumes that the input `n` is a positive integer. If the input can be negative or zero, additional checks and handling would be needed.