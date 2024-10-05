```javascript
function fib(n) {
  if (n <= 1) return n;
  let a = 0, b = 1, result = 1;
  for (let i = 2; i <= n; i++) {
    result = a + b;
    a = b;
    b = result;
  }
  return result;
}

console.log(fib(10)); // 55
console.log(fib(1)); // 1
console.log(fib(8)); // 21
```
This function uses an iterative approach to calculate the nth Fibonacci number. It keeps track of the last two Fibonacci numbers (a and b) and updates them in each iteration. The result is the nth Fibonacci number. The function also handles the base cases where n is 0 or 1, returning n directly in these cases. The time complexity of this function is O(n), which is more efficient than the recursive approach. The space complexity is O(1), as it only uses a constant amount of space to store the variables a, b, and result.