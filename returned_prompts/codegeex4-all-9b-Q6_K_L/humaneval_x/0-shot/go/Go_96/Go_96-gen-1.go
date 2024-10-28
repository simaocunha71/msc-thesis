To solve this problem, we need to implement a function that takes an non-negative integer n and returns an array of the first n integers that are prime numbers and less than n. 

Here is the implementation in Go:

```go
func CountUpTo(n int) []int {
    primes := []int{}

    for i := 2; i < n; i++ {
        isPrime := true

        for j := 2; j < i; j++ {
            if i%j == 0 {
                isPrime = false
                break
            }
        }

        if isPrime {
            primes = append(primes, i)
        }

        if len(primes) == n {
            break
        }
    }

    return primes
}
```

Explanation:
1. We start by creating an empty slice `primes` to store the prime numbers.
2. We iterate from 2 to n-1 using a for loop.
3. For each number i, we check if it is prime by iterating from 2 to i-1 using another for loop.
4. If i is divisible by any number j (i.e., i%j == 0), it is not a prime number, so we set `isPrime` to false and break out of the inner loop.
5. If `isPrime` is still true after the inner loop, it means i is a prime number, so we append it to the `primes` slice.
6. We also check if the length of the `primes` slice is equal to n. If it is, we break out of the outer loop as we have found the first n prime numbers.
7. Finally, we return the `primes` slice.

Note: This implementation has a time complexity of O(n^2) because it checks each number from 2 to n-1 for primality. There are more efficient algorithms for finding prime numbers, such as the Sieve of Eratosthenes, but this implementation is simple and easy to understand.