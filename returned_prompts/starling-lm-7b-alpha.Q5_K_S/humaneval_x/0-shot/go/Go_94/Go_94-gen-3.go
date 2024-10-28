To solve this problem, you can follow these steps:

1. Find the largest prime value in the given list.
2. Convert the prime value to a string.
3. Iterate through each character of the string and add its numeric value to the sum.
4. Return the sum of the digits.

Here's the detailed solution in Go:

```go
package main

import (
    "math"
    "strconv"
    "sort"
)

func Skjkasdkd(lst []int) int {
    maxPrime := -1
    maxPrimeIndex := -1

    for i, v := range lst {
        if isPrime(v) && v > maxPrime {
            maxPrime = v
            maxPrimeIndex = i
        }
    }

    strMaxPrime := strconv.Itoa(maxPrime)
    sum := 0

    for _, v := range strMaxPrime {
        sum += int(v - '0')
    }

    return sum
}

func isPrime(n int) bool {
    if n <= 1 {
        return false
    }
    if n <= 3 {
        return true
    }
    if n%2 == 0 || n%3 == 0 {
        return false
    }
    i := 5
    for ; i * i <= n; i += 6 {
        if n%i == 0 || n%(i + 2) == 0 {
            return false
        }
    }
    return true
}
```

The `isPrime` function checks if a number is prime by performing a basic primality test. It first checks if the number is less than or equal to 1, in which case it's not prime. Then it checks if the number is less than or equal to 3, in which case it's prime. If the number is greater than 3, it checks if it's divisible by 2 or 3, in which case it's not prime. Finally, it iterates through all multiples of 6 starting from 5 and checks if the number is divisible by any of them, in which case