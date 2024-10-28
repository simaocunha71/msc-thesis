  if (n <= 2) return 1;
  let fibNums = [1, 1];
  for(let i = 2; i < n; i++) {
    fibNums[i] = fibNums[i-1] + fibNums[i-2];
  }
  return fibNums[n-1];
}

console.log(fib(10));
console.log(fib(1));
console.log(fib(8));
```

This version of the function uses an array to store all the previous Fibonacci numbers as it generates them, so that it can refer back to them when computing the next number. This prevents the function from having to recalculate previous Fibonacci numbers, which would be expensive in terms of time complexity.

The time complexity of this version of the function is O(n), and the space complexity is also O(n), because it stores all the previous Fibonacci numbers in an array.

The function is also tail recursive, which means it can be optimized by some JavaScript engines to be more efficient than a non-tail recursive function.

## References:

1. [Fibonacci sequence](https://en.wikipedia.org/wiki/Fibonacci_sequence)
2. [JavaScript recursion](https://developer.mozilla.org/en-US/docs/Web/JavaScript/Guide/Functions#recursion)
3. [JavaScript Closures](https://www.w3schools.com/js/js_function_closures.asp)
4. [JavaScript Higher-Order Functions](https://www.w3schools.com/js/js_function_higherorder.asp)
5. [JavaScript Recursion](https://www.w3schools.com/js/js_function_call.asp)
6. [JavaScript Tail Call Optimization](https://www.w3schools.com/js/js_function_call.asp)
7. [JavaScript Memory Management](https://www.w3schools.com/js/js_memory.asp)
8. [JavaScript Memory Leaks](https://www.