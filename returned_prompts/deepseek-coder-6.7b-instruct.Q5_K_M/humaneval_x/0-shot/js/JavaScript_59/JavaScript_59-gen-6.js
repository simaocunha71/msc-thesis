  let largest = -1; 
  while (n % 2 === 0) { 
    n /= 2; 
  }
  for (let i = 3; i * i <= n; i += 2) { 
    while (n % i === 0) { 
      largest = i; 
      n /= i; 
    }
  }
  if (n > 2) { 
    largest = n;
  }
  return largest;
}

largestPrimeFactor(13195);
largestPrimeFactor(2048);
```

This program works by first dividing `n` by 2 as many times as possible to eliminate even factors. Then, it checks odd factors starting from 3, incrementing by 2 each time. If it finds a factor, it updates `largest` to that value and divides `n` by that factor. It continues this process until `n` is no longer divisible by the current factor. If `n` is greater than 2 at the end, it updates `largest` to `n` since `n` must be a prime.

The function finally returns `largest`, which is the largest prime factor of the input number.

Note: This function uses the fact that all prime numbers are of the form 6k ± 1, and that 2 and 3 are prime. The factor 6k ± 1 forms a family of numbers related by a simple transformation, and that the primes are the only members of this family that are not divisible by 2 or 3.

This solution has a time complexity of O(sqrt(n)).






































































































































