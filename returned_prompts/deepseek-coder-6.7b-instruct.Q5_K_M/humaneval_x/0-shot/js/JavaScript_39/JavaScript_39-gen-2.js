  const isPrime = (num) => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  const fibonacci = (n) => {
    let a = 1, b = 1;
    while(n-- > 0){
      [a, b] = [b, a + b];
    }
    return a;
  }

  let count = 0, result = 0;
  for(let i = 1;; i++){
    const fib = fibonacci(i);
    if(isPrime(fib)){
      count++;
      result = fib;
    }
    if(count === n) return result;
  }
}

module.exports = primeFib;
```

This solution first checks if a number is a prime number or not by checking if it can be divided evenly by any numbers up to its square root. If it cannot, then it is a prime number. 

Next, it creates a function to generate Fibonacci numbers by starting with two 1's and then continuously adding the two most recent numbers.

Finally, it creates a loop that will keep generating Fibonacci numbers and checking if they are prime until it reaches the nth prime Fibonacci number.

This code has a time complexity of O(n^2) because it iterates over the Fibonacci sequence, and for each Fibonacci number, it checks if it's a prime number by iterating up to its square root.

This code has a space complexity of O(1) because it only uses a constant amount of space to store the Fibonacci numbers, the count, and the result.

The tests for this solution are in the file test.js.

```
const primeFib = require('./primeFib');

console.log(primeFib(1)); // 2
console.log(primeFib(2)); // 3
console.log(primeFib(3)); // 5
console.log(primeFib(4)); // 13