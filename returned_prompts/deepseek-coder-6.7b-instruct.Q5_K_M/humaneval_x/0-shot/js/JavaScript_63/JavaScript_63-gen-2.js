  if (n < 0) {
    return 'Input should be a non-negative integer';
  }
  if (n === 0 || n === 1) {
    return 0;
  }
  if (n === 2) {
    return 1;
  }

  let fib = [0, 0, 1];

  for (let i = 3; i <= n; i++) {
    fib[i] = fib[i-1] + fib[i-2] + fib[i-3];
  }

  return fib[n];
};

console.log(fibfib(1)); // 0
console.log(fibfib(5)); // 4
console.log(fibfib(8)); // 24

```

Here we are storing the previous three numbers of the sequence in an array and using them to calculate the next number. This is more efficient than a recursive solution, which can be slow due to repeated calculations of the same values.

Please note that this solution assumes that n is a non-negative integer. If you want to handle other types of input, you'll need to add error checking for that.

Also note that this solution has a space complexity of O(n) because it stores all the previous numbers in the sequence. If you only needed to calculate the last number, you could optimize it to have a space complexity of O(1) by only storing the last three numbers.

The time complexity of this solution is O(n), as it calculates the n-th number by looping from 3 to n.

```

```python

