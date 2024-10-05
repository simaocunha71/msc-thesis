  if(n <= 2){
    return 1;
  }
  let prev = 1;
  let curr = 1;
  for(let i = 3; i <= n; i++){
    let temp = curr;
    curr += prev;
    prev = temp;
  }
  return curr;
}

console.log(fib(10)); // 55
console.log(fib(1));  // 1
console.log(fib(8));  // 21

```

This code defines a function `fib` that computes the nth Fibonacci number. It uses an iterative approach to compute the Fibonacci numbers. The base cases are when n is 1 or 2. For n > 2, it initializes two variables `prev` and `curr` to 1, then enters a loop that iterates n - 2 times. At each iteration, it computes the next Fibonacci number as the sum of `prev` and `curr`, and then updates `prev` to `curr` and `curr` to the new sum. Finally, it returns `curr` as the nth Fibonacci number.

This function is efficient because it has a time complexity of O(n) and a space complexity of O(1), making it suitable for computing large Fibonacci numbers.

```javascript
