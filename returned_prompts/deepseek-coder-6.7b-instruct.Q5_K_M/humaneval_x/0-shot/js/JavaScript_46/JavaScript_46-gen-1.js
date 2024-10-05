  if (n < 2) return 0;
  if (n === 2) return 2;
  if (n === 3) return 0;

  let a = 0;
  let b = 0;
  let c = 2;
  let d = 0;
  let res = 0;

  for (let i = 4; i <= n; i++) {
    res = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = res;
  }

  return res;
};

module.exports = fib4;
```

This solution utilizes the dynamic programming approach to compute the n-th element of the fib4 number sequence. The time complexity of this solution is O(n) and the space complexity is O(1), which makes it highly efficient.

## Solution:

```javascript
// Fib4 Sequence
const fib4 = (n) => {
  if (n < 2) return 0;
  if (n === 2) return 2;
  if (n === 3) return 0;

  let a = 0;
  let b = 0;
  let c = 2;
  let d = 0;
  let res = 0;

  for (let i = 4; i <= n; i++) {
    res = a + b + c + d;
    a = b;
    b = c;
    c = d;
    d = res;
  }

  return res;
};

console.log(fib4(5)); // 4
console.log(fib4(6)); // 8
console.log(fib4(7)); // 14
```

This solution utilizes the dynamic programming approach to compute the n-th element of the fib4 number sequence. The time complexity of this solution is O(n) and the space complexity is O(1), which makes it highly efficient.

## Explanation:

In the solution, we first handle the base cases where `n` is less than 2, equal to 2, or equal to 3. For `n` less than 2, we return 0, for