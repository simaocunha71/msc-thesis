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

Explanation:
The function `largestDivisor` takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`. The function iterates from `n-1` down to `2` (inclusive) and checks if each number is a divisor of `n` using the modulo operator (`%`). If a divisor is found, it is immediately returned. If no divisors are found, the function returns `1` (since `1` is a divisor of every number). In the given example, the largest divisor of `15` is `5`, which is returned by the function. 

The time complexity of this function is O(n), where n is the input number, because in the worst-case scenario, the function needs to iterate up to `n-1` times to find the largest divisor. The space complexity is O(1), as the function only uses a constant amount of space to store the variables. 

The function can be optimized further by starting the iteration from `Math.sqrt(n)` instead of `n-1`, since a larger factor of the number would be a multiple of smaller factor that has already been checked. This optimization reduces the time complexity to O(√n). 

Here is the optimized function:
```
function largestDivisor(n) {
  for (let i = Math.sqrt(n); i > 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
}
``` 