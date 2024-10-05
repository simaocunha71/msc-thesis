Here's one way to solve this problem:

1. Initialize an empty object, `primes`, to store the prime factors of `n`.

2. Iterate through each prime number, `p`, from 2 to the square root of `n`.

3. While `n` is divisible by `p`, do the following:

   a. If `p` is not in `primes`, add `p` as a key to `primes` with an initial value of 0.
   
   b. Increment the value of `p` in `primes` by 1.
   
   c. Divide `n` by `p`.

4. If `n` is greater than 1, add `n` as a key to `primes` with an initial value of 1.

5. Convert the `primes` object to an array, `arr`, using the spread operator.

6. Sort `arr` in ascending order.

7. Return `arr`.

The time complexity of this algorithm is O(sqrt(n)), as we only need to check primes up to the square root of `n`. The space complexity is O(n), as we store each prime factor in the `primes` object.

Here's the Python code to implement this algorithm:

```python
def factorize(n):
    primes = {}
    p = 2
    while n > 1 and p * p <= n:
        while n % p == 0:
            n //= p
            if p not in primes:
                primes[p] = 0
            primes[p] += 1
        p += 1

    if n > 1:
        primes[n] = 1

    return list(primes.keys())
```

And here's the JavaScript code to implement this algorithm:

```javascript
function factorize(n) {
    let primes = {};
    let p = 2;
    while (n > 1 && p * p <= n) {
        while (n % p == 0) {
            n /= p;
            if (p in primes === false) {
                primes