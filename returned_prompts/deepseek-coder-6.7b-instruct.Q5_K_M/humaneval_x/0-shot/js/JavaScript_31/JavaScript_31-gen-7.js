  if (n < 2) {
    return false;
  }
  for (let i = 2; i < n; i++) {
    if (n % i === 0) {
      return false;
    }
  }
  return true;
}

module.exports = isPrime;
```

This function takes a number as an input and checks whether it is prime or not. If the number is less than 2, it returns false since prime numbers are greater than 1. Then it uses a for loop to check for any factors of the input number. If it finds any, it returns false. If it does not find any factors, it returns true, indicating that the number is prime.

Please note that the function will work correctly for small numbers, but for very large numbers, it would be more efficient to use a more sophisticated algorithm like the Sieve of Eratosthenes.

Also, keep in mind that this is a simple function and does not cover all the potential edge cases. For example, it does not handle negative numbers or non-integer inputs. You might want to add some error checking to handle these cases.

Finally, this function is not optimized for large numbers. If you need to check large numbers, you might want to use a more efficient algorithm like the Sieve of Eratosthenes.

Testing:

You can test this function using a variety of inputs to ensure it is working as expected. You can use a testing library like Jest to easily create tests for your function.

For example:

```javascript
const isPrime = require('./isPrime');

test('Check if 6 is prime', () => {
  expect(isPrime(6)).toBe(false);
});

test('Check if 101 is prime', () => {
  expect(isPrime(101)).toBe(true);
});

// Add more tests as needed
```

This will test if the function correctly identifies 6 as not prime and 101 as prime. You can add more tests to cover all the edge cases and potential inputs for your function.

I hope this helps explain how to create a basic prime checking function in JavaScript. If you have any more questions, feel free to ask.


```javascript
// Function to check