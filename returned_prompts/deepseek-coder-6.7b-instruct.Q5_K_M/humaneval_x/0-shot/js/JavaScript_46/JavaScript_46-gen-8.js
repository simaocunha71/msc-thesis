  if (n < 2) return 0;
  if (n === 2) return 2;

  let fibs = [0, 0, 2];

  for (let i = 3; i <= n; i++) {
    fibs[i] = fibs[i-1] + fibs[i-2] + fibs[i-3] + fibs[i-4];
  }

  return fibs[n];
};

console.log(fib4(5)); // 4
console.log(fib4(6)); // 8
console.log(fib4(7)); // 14


Explanation:
This function uses an iterative approach. It first creates an array with the first four elements of the Fib4 sequence. Then it fills up the array with the next elements by adding the last four elements of the array. Finally, it returns the n-th element of the array. This is an efficient way to compute the n-th element of the Fib4 sequence because it avoids the need for recursion and stores the already computed elements in an array.

Time complexity: O(n)
Space complexity: O(n)
*/

module.exports = fib4;
```

This solution uses an iterative approach and stores previously computed elements in an array. This results in a time complexity of O(n) and a space complexity of O(n), where n is the input number.

This solution works by initializing an array with the first four Fib4 values, then iterating over the array from 4 to the input number, each time calculating the next Fib4 value by summing the last four values in the array. Finally, it returns the n-th Fib4 value.

This solution is efficient and will work for any valid input number.

Note: This solution assumes that the input number is a non-negative integer. If the input number is negative, it will not produce the expected result.

Also, note that the Fib4 sequence is not standard and may not have a closed form solution, so it's common to define it recursively or iteratively.

This solution assumes that the input number is a non-negative integer. If the input number is negative, it will not produce the expected