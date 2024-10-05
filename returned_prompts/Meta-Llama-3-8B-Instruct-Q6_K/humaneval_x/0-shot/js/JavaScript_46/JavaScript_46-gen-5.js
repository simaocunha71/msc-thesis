Here is the solution for the problem. The idea is to use a loop to calculate the first n numbers in the sequence and store them in an array. Then we can return the nth number in the array.

```javascript
const fib4 = (n) => {
  if (n <= 1) {
    return 0;
  }
  if (n === 2) {
    return 2;
  }
  const fib4Array = [0, 0, 2, 0];
  for (let i = 4; i <= n; i++) {
    fib4Array.push(fib4Array[i - 1] + fib4Array[i - 2] + fib4Array[i - 3] + fib4Array[i - 4]);
  }
  return fib4Array[n - 1];
};
```

This function works by creating an array to store the first n numbers in the sequence. It starts by initializing the array with the first four numbers in the sequence, then it loops through the rest of the sequence, calculating each number as the sum of the previous four numbers. Finally, it returns the nth number in the array. This approach has a time complexity of O(n) and a space complexity of O(n), which is efficient for calculating the nth number in the sequence.