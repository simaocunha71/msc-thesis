```javascript
function largestDivisor(n) {
  for (let i = n - 1; i > 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
}

console.log(largestDivisor(15)); // Output: 5
```



Explanation:

This function `largestDivisor` takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. It does this by iterating from `n-1` down to `1` and checking each number to see if it divides `n` evenly. If it finds a number that divides `n` evenly, it returns that number. If it reaches `1` without finding a divisor, it returns `1`.

In the example, `largestDivisor(15)` returns `5` because `5` is the largest number that divides `15` evenly, smaller than `15`.