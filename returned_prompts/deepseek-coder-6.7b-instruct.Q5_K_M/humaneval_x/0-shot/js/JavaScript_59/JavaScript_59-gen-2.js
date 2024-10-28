  let factor = 2;

  while (factor <= n) {
    if (n % factor === 0) {
      n = n / factor;
    } else {
      factor++;
    }
  }

  return factor;
};

console.log(largestPrimeFactor(13195)); // 29
console.log(largestPrimeFactor(2048)); // 2
```

This function works by starting with the smallest prime number, 2, and continuously dividing `n` by this factor as long as `n` is divisible by it. If `n` is not divisible by the factor, the factor is incremented and the process is repeated. The last factor that was successfully divided into `n` is the largest prime factor.

In the first example, the prime factors of 13195 are 29, 11, and 7, so the function returns 29.
In the second example, the prime factor of 2048 is 2, so the function returns 2.

The time complexity of this function is O(n) as it loops from 2 to `n`. The space complexity is O(1) because it uses a constant amount of space to store the factor and the result.

The function is correct and efficient for the given problem constraints.
*/
```

The function works by starting with the smallest prime number, 2, and continuously dividing `n` by this factor as long as `n` is divisible by it. If `n` is not divisible by the factor, the factor is incremented and the process is repeated. The last factor that was successfully divided into `n` is the largest prime factor.

In the first example, the prime factors of 13195 are 29, 11, and 7, so the function returns 29.
In the second example, the prime factor of 2048 is 2, so the function returns 2.

The time complexity of this function is O(n) as it loops from 2 to `n`. The space complexity is O(1) because it uses a constant amount of space to store the factor and the result.

The function is correct and efficient for the