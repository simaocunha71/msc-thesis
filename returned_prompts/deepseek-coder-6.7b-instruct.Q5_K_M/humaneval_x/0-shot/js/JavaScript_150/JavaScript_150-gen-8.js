  const isPrime = num => {
    for(let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if(num % i === 0) return false; 
    return num > 1;
  }

  return isPrime(n) ? x : y;
}

console.log(xOrY(7, 34, 12)); // 34
console.log(xOrY(15, 8, 5)); // 5
console.log(xOrY(2, 10, 20)); // 10
console.log(xOrY(4, 30, 40)); // 40
console.log(xOrY(6, 60, 70)); // 70
```

In this JavaScript function, first we create a helper function `isPrime()` which checks if a number `n` is a prime number. If it is a prime number, it returns `true`, otherwise `false`. Then, in the main function `xOrY()`, we return the value of `x` if `n` is a prime number, and the value of `y` otherwise.

This function uses a simple method to check if a number is prime: it divides the number by all numbers less than its square root and checks if the remainder is 0. If the remainder is 0, then the number is not prime. If no remainder is found, then the number is prime. The reason we only need to check up to the square root of `n` is that a larger factor of the number would be a multiple of a smaller factor that has already been checked.

This function can be used to make decisions based on whether a number is prime. For example, in a game, if a player's score is a prime number, they might receive a special bonus.

```javascript
// Usage
console.log(xOrY(7, 'prime', 'not prime')); // 'prime'
console.log(xOrY(15, 'prime', 'not prime')); // 'not prime'
```
In the above usage, if the number is prime, it will return 'prime', otherwise 'not prime'.
```


### 