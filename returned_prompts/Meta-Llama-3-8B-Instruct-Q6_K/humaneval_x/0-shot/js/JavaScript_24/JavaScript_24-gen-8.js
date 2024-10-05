Here is a possible implementation of the `largestDivisor` function in JavaScript:
```
const largestDivisor = (n) => {
  for (let i = n - 1; i > 0; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
};
```
This function uses a simple loop to iterate from `n-1` down to `1`, and checks if each number is a divisor of `n` using the modulo operator (`%`). If it finds a divisor, it returns that number. If it reaches the end of the loop without finding a divisor, it returns `1` (since `1` is always a divisor of any number).

You can test this function with the example input `15`:
```
console.log(largestDivisor(15)); // Output: 5
```
This implementation has a time complexity of O(n), since it iterates from `n-1` down to `1`. If you need a more efficient solution, you can use a more advanced algorithm, such as the `Math.floor(Math.sqrt(n))` trick, which can reduce the time complexity to O(√n). Here is an updated implementation:
```
const largestDivisor = (n) => {
  for (let i = Math.floor(Math.sqrt(n)); i > 0; i--) {
    if (n % i === 0) {
      return i;
    }
  }
  return 1;
};
```
This implementation uses the `Math.floor(Math.sqrt(n))` trick to reduce the search space to the range `[1, √n]`, which can significantly improve performance for large inputs. However, for small inputs, the simple loop-based implementation may be sufficient.