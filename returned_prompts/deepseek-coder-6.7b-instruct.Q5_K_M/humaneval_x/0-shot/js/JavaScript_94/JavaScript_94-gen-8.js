  // First, we need to find the largest prime number in the list
  let largestPrime = Math.max(...lst.filter(isPrime));

  // Then we convert the number to a string and split the digits into an array
  let digits = Array.from(String(largestPrime), Number);

  // Finally, we sum up all the digits in the array
  let sumOfDigits = digits.reduce((a, b) => a + b, 0);

  // We return the sum of the digits
  return sumOfDigits;
}

const isPrime = (n) => {
  if (n < 2) return false;
  for (let i = 2; i * i <= n; i++) {
    if (n % i === 0) return false;
  }
  return true;
}
```

This solution first filters the input list to find all prime numbers, then finds the maximum of these primes. After that, it splits the largest prime number into its digits and sums them up. The function `isPrime` is used to check if a number is a prime number.

This solution works in O(n) time complexity where n is the length of the list.

The isPrime function works in O(sqrt(n)) time complexity.

The main function works in O(n) time complexity.

Therefore the overall time complexity is O(n sqrt(n)).

This solution works in O(d) space complexity where d is the number of digits in the largest prime number.

So the space complexity is O(log n) for the input list and O(d) for the largest prime number.

Therefore, the total space complexity is O(n + log n) which can be simplified to O(n).

This solution assumes that the input list contains at least one prime number.

Please note that in JavaScript, the Math.max function cannot be used with an array of zero elements. It will throw a RangeError. So, we must ensure that our array is not empty before applying the Math.max function.

Also, this solution assumes that all elements in the list are positive integers. If the list can contain negative numbers or non-integers, additional checks