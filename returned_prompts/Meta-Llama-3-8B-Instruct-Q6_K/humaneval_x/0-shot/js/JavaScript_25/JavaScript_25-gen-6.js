```
function factorize(n) {
  const factors = [];
  let i = 2;
  while (i * i <= n) {
    while (n % i === 0) {
      factors.push(i);
      n /= i;
    }
    i += 1;
  }
  if (n > 1) {
    factors.push(n);
  }
  return factors;
}
```


This function takes an integer `n` as input and returns a list of its prime factors. The list is ordered from smallest to largest, and each factor is listed the number of times it appears in the factorization of `n`.

Here's how it works:

1. We start by initializing an empty list `factors` that will store the prime factors of `n`.
2. We set `i` to 2, the smallest prime number, and loop until `i * i` is greater than `n`.
3. Inside the loop, we check if `n` is divisible by `i` (i.e., `n % i === 0`). If it is, we add `i` to the `factors` list and divide `n` by `i`. This process continues until `n` is no longer divisible by `i`.
4. We increment `i` by 1 and repeat step 3 until `i * i` is greater than `n`.
5. If `n` is still greater than 1 after the loop, it means that `n` is a prime number itself, so we add it to the `factors` list.
6. Finally, we return the `factors` list.

This function uses the fact that every composite number can be expressed as a product of prime numbers, and that each prime factor can be found by dividing the number by the smallest prime number that divides it. The function is efficient because it uses a while loop to iterate over the prime numbers and only adds each prime factor to the list once.