```
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


In this solution, we start from the number just before `n` and keep decreasing the number until we find a number that divides `n` evenly. We use the modulo operator (`%`) to check if the current number is a divisor of `n`. If it is, we return the number. If we reach 1 and haven't found a divisor, we return 1, since 1 is the smallest divisor of any number.

The time complexity of this solution is O(n), where n is the input number, since we iterate from `n-1` down to 1. The space complexity is O(1), since we only use a constant amount of space to store the current number and the result.