To solve this problem, we need to find the largest prime number in the given list and then return the sum of its digits. Here's how we can do it:

1. Create a helper function to check if a number is prime. This function will take a number as input and return `true` if it is prime and `false` otherwise.
2. Iterate through the list of numbers and check if each number is prime using the helper function.
3. Keep track of the largest prime number encountered so far.
4. Once we have found the largest prime number, we can return the sum of its digits by converting it to a string and summing up the digits.

Here's the code for the `skjkasdkd` function:

```javascript
const skjkasdkd = (lst) => {
  // Helper function to check if a number is prime
  const isPrime = (num) => {
    if (num <= 1) return false;
    for (let i = 2; i <= Math.sqrt(num); i++) {
      if (num % i === 0) return false;
    }
    return true;
  };

  // Initialize the largest prime number as -1
  let largestPrime = -1;

  // Iterate through the list of numbers
  for (let i = 0; i < lst.length; i++) {
    if (isPrime(lst[i]) && lst[i] > largestPrime) {
      largestPrime = lst[i];
    }
  }

  // Return the sum of the digits of the largest prime number
  return largestPrime.toString().split('').reduce((acc, digit) => acc + parseInt(digit), 0);
};
```

Let's test the function with the provided examples:

```javascript
console.log(skjkasdkd([0,3,2,1,3,5,7,4,5,5,5,2,181,32,4,32,3,2,32,324,4,3])); // 10
console.log(skjkasdkd([1,0,1,8,2,4597,2,1,3,40,1,2,1,2,4,2,5,1])); // 25
console.log(skjkasdkd([1,3,1,32,5107,34,83278,109,163,23,2323,32,30,1