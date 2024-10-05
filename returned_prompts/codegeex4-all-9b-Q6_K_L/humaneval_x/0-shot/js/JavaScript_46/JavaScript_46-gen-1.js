The Fib4 number sequence is a sequence similar to the Fibbonacci sequnece that's defined as follows:
fib4(0) -> 0
fib4(1) -> 0
fib4(2) -> 2
fib4(3) -> 0
fib4(n) -> fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).
Please write a function to efficiently compute the n-th element of the fib4 number sequence. Do not use recursion.
To solve this problem, we can use an iterative approach to compute the n-th element of the Fib4 number sequence. We will start by initializing an array of size n+1 to store the Fib4 numbers. Then, we will iterate from 4 to n and compute each Fib4 number by summing the previous four Fib4 numbers. Finally, we will return the n-th Fib4 number.

Here is the implementation in JavaScript:

```javascript
const fib4 = (n) => {
  // Initialize an array of size n+1 to store the Fib4 numbers
  const fib4Arr = new Array(n + 1).fill(0);

  // Set the first four Fib4 numbers
  fib4Arr[0] = 0;
  fib4Arr[1] = 0;
  fib4Arr[2] = 2;
  fib4Arr[3] = 0;

  // Compute each Fib4 number by summing the previous four Fib4 numbers
  for (let i = 4; i <= n; i++) {
    fib4Arr[i] = fib4Arr[i - 1] + fib4Arr[i - 2] + fib4Arr[i - 3] + fib4Arr[i - 4];
  }

  // Return the n-th Fib4 number
  return fib4Arr[n];
};
```

Now, we can test the function with the given examples:

```javascript
console.log(fib4(5)); // Output: 4
console.log(fib4(6)); // Output: 8
console.log(fib4(7)); // Output: 14
```

The function correctly computes the n-th element of the Fib4 number sequence without using recursion.