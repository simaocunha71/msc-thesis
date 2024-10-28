for (let i = n-1; i >= 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
}

console.log(largestDivisor(15));

```

This function starts from n-1 and keeps going down until it finds a number that divides evenly into n. 

It's important to note that this function will not work correctly if the number entered is less than or equal to zero, because the loop will run backwards from 0 which is not a valid input. We should add a validation check for this.

```javascript
const largestDivisor = (n) => {
  if(n <= 0) {
    return 'Invalid input, enter a positive number greater than zero';
  }
  
  for (let i = n-1; i >= 1; i--) {
    if (n % i === 0) {
      return i;
    }
  }
}

console.log(largestDivisor(15)); // 5
console.log(largestDivisor(-15)); // 'Invalid input, enter a positive number greater than zero'
```

This function now checks if the input number is less than or equal to zero, and if so, it returns an error message.

### Step-by-Step Breakdown

1. Define a function named `largestDivisor` that takes one parameter `n`.
2. Inside the function, check if `n` is less than or equal to zero. If it is, return the string `'Invalid input, enter a positive number greater than zero'`.
3. If `n` is greater than zero, start a for loop that starts at `n-1` and runs down to 1.
4. In the for loop, check if `n` divided by the current number `i` has a remainder of 0 (`n % i === 0`). If it does, return `i` as the largest divisor of `n`.
5. If the for loop finishes without finding a divisor, `n` is a prime number and there is no largest divisor other than 1. Return 1.

This function works by checking if `n` is divisible by each number less than