  if (n < 0) {
    return 'Input should be a positive integer';
  } 

  let fibfibSequence = [0, 0, 1];

  for(let i = 3; i <= n; i++) {
    fibfibSequence[i] = fibfibSequence[i-1] + fibfibSequence[i-2] + fibfibSequence[i-3];
  }

  return fibfibSequence[n];
};

console.log(fibfib(1)); // 0
console.log(fibfib(5)); // 4
console.log(fibfib(8)); // 24

In this solution, we first handle the base cases where n is less than 3. Then we initialize an array fibfibSequence to hold the first three values of the sequence. After that, we loop from 3 to n (inclusive) and calculate the next value in the sequence as the sum of the previous three values. Finally, we return the n-th value in the sequence.

The time complexity of this solution is O(n) because we iterate from 3 to n and the space complexity is also O(n) because we store the whole sequence up to n in an array.

This solution is efficient as it avoids the problem of redundant calculations in the naive recursive solution by storing the previously computed values in an array.

However, there is also a O(1) space complexity solution by using only three variables to store the last three values of the sequence:

const fibfib 2 = n => {
  if (n < 0) {
    return 'Input should be a positive integer';
  }

  if (n < 3) {
    return n == 2 ? 1 : 0;
  }

  let a = 0, b = 0, c = 1, d;

  for(let i = 3; i <= n; i++) {
    d = a + b + c;
    a = b;
    b = c;
    c = d;
  }

  return d;
};

console.log(fibfib2(1)); // 0
console.log(fib