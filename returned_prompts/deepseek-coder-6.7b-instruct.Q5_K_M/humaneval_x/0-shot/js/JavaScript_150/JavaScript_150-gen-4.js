  const isPrime = num => {
    for (let i = 2, sqrt = Math.sqrt(num); i <= sqrt; i++)
      if (num % i === 0) return false;
    return num > 1;
  }

  return isPrime(n) ? x : y;
}
console.log(xOrY(7, 34, 12)) // 34
console.log(xOrY(15, 8, 5)) // 5



/*
  The function 'isPrime' checks if the number passed to it is a prime number by 
  checking if any number from 2 to the square root of the number evenly 
  divides it. If it does, the function returns false, meaning the number is not prime.
  If it doesn't find any such number, it returns true, meaning the number is prime.
  The function 'xOrY' then uses a ternary operator to return the value of x if n is 
  prime, and the value of y otherwise.
*/

```

## Question 2:

```javascript
