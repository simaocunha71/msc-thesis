  if (n <= 1) return false;
  if (n <= 3) return true;
  if (n % 2 === 0 || n % 3 === 0) return false;

  let i = 5;

  while (i * i <= n) {
    if (n % i === 0 || n % (i + 2) === 0) return false;
    i += 6;
  }

  return true;
};

console.log(isPrime(6)); // false
console.log(isPrime(101)); // true
console.log(isPrime(11)); // true
console.log(isPrime(13441)); // false
console.log(isPrime(61)); // true
console.log(isPrime(4)); // false
console.log(isPrime(1)); // false
```

This solution first checks if the number is less than or equal to 1, which it is, and if it is, it returns `false`. It then checks if the number is less than or equal to 3, which it is, and if it is, it returns `true`. After that, it checks if the number is divisible by 2 or 3, in which case it returns `false`.

The while loop then checks if the number is divisible by any number between 5 and the square root of the number. If it is, it returns `false`. The increment `i += 6` is used to skip multiples of 2 and 3, since we have already checked for divisibility by 2 and 3.

Finally, if the number has not been identified as divisible by any of the tested numbers, it is a prime number, so the function returns `true`.

The time complexity of this solution is `O(sqrt(n))`, because in the worst case, the function checks up to the square root of `n` for factors.

The space complexity is `O(1)`, because no additional space is used that scales with the size of the input.

This solution is based on the fact that all primes are of the form 6k ± 1, with the exception of 2 and 3. This allows us to skip checking for factors