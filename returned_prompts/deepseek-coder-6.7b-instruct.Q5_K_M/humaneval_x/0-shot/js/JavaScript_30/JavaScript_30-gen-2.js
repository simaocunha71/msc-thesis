  return l.filter(n => n > 0)
}


//Test cases
console.log(getPositive([-1, 2, 5, 6])) //[2, 5, 6]
console.log(getPositive([5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10])) //[5, 3, 2, 3, 9, 123, 1]
```

### 2. Filtering for Prime Numbers

Write a function `getPrimes(l)` that takes in an array of integers and returns a new array that only contains the prime numbers from the input array.

A prime number is a natural number greater than 1 that has no positive divisors other than 1 and itself. The first few prime numbers are 2, 3, 5, 7, 11, and 13.

To check if a number is prime, you would start by checking if the number is greater than 1. Then you would check for any divisors other than 1 and itself. If you find any, the number is not prime. Otherwise, it is prime.

```javascript
