  if (n < 2) return 0;
  if (n === 2) return 1;

  let a = 0;
  let b = 0;
  let c = 1;

  for (let i = 3; i <= n; i++) {
    const temp = c;
    c += a + b;
    a = b;
    b = temp;
  }

  return c;
};

console.log(fibfib(1)); // 0
console.log(fibfib(5)); // 4
console.log(fibfib(8)); // 24

```

Explanation:
In this solution, we initialize three variables `a`, `b` and `c` to represent the `n-3`, `n-2` and `n-1` terms of the sequence respectively. Then we start a loop from 3 to `n` and in each iteration, we calculate the `n-th` term as the sum of `a`, `b` and `c` and then shift the values of `a` and `b` to represent the last two terms of the sequence. Finally, we return `c` which is the `n-th` term of the sequence.

The time complexity of this solution is O(n) and the space complexity is O(1), which means it uses constant space.

Please note that, due to the nature of the problem, the function will return `undefined` for negative inputs and for non-integer inputs.
*/

// Do not edit below this line
module.exports = fibfib;
```














































































































































