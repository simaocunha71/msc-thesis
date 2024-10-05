One way to solve this kata is to use the following steps:

1. Initialize an empty array called `factors` to store the prime factors.
2. Create a loop to iterate from 2 to `n`.
3. Check if `n` is divisible by the current iteration number (i). If it is, then:
   a. Divide `n` by i and store the quotient in `n`.
   b. Push i to the `factors` array.
   c. Repeat steps 3a and 3b until `n` is no longer divisible by i.
4. Return the `factors` array.

Here's a Python implementation of the above algorithm:

```python
def factorize(n):
    factors = []
    i = 2
    while n > 1:
        while n % i == 0:
            factors.append(i)
            n //= i
        i += 1
    return factors
```

This implementation starts with `i` equal to 2 and continues until `n` is no longer divisible by `i`. For every `i` that divides `n`, it appends `i` to the `factors` list and updates `n` by dividing it by `i`. The `i` value is incremented by 1 after each iteration of the inner loop. This process continues until `n` is reduced to 1, at which point the `factors` list contains all the prime factors of the original number `n`.

The time complexity of this algorithm is O(sqrt(n)), as the largest potential factor of `n` is its square root. The space complexity is O(log(n)), as the number of factors in the `factors` list can be at most log(n).

For example, if you call `factorize(8)`, the algorithm will start with `i` equal to 2. It will divide 8 by 2, resulting in a quotient of 4. Since 4 is still divisible by 2, it will append 2 to the `factors` list and update `n` to 4. The next time through the loop, `i` will be 3, but 4 is not divisible by 3, so the loop will