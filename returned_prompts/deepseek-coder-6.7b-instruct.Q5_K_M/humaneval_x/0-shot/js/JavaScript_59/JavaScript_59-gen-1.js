  let largest = -1;

  while (n % 2 === 0) {
    largest = 2;
    n >>= 1;
  }

  for (let i = 3; i <= Math.sqrt(n); i += 2) {
    while (n % i === 0) {
      largest = i;
      n = n / i;
    }
  }

  if (n > 2) {
    largest = n;
  }

  return largest;
};

console.log(largestPrimeFactor(13195)); //29
console.log(largestPrimeFactor(2048)); //2
```

The main idea here is to divide the input number n by 2 until it's no longer divisible. This is because 2 is the only even prime number. After that, we start checking from 3 up to the square root of n. We increment by 2 each time because even numbers are not prime. If n is still greater than 2 after this, then it means n is a prime number and is the largest prime factor.

It's worth noting that this algorithm works because of the properties of prime numbers. A prime number is a number that has exactly two distinct natural number divisors: 1 and itself. This means that if n is not a prime, then it must have at least one factor other than 1 and itself. The largest of these factors will be the largest prime factor of n.

Also, the square root of n is used as the upper limit for the loop because a larger factor of n would be a multiple of some smaller factor that has already been checked.

Finally, the bitwise shift operator (>>=) is used to divide n by 2. This is more efficient than using the division operator (/=) because bitwise operators are faster.

This algorithm has a time complexity of O(sqrt(n)) because it checks up to the square root of n for factors.
*/

// export { largestPrimeFactor };

// export default largestPrimeFactor;
module.exports = largestPrimeFactor;

/*
To use this function, just import it in your program and call it with the number you want to find the largest prime factor of. For example:

