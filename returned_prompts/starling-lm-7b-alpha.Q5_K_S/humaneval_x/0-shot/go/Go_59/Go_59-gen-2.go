
To solve this problem, we can use a while loop to keep dividing the input number by the largest prime factor until it becomes 1. Here's the step-by-step process:

1. Initialize a variable "prime" to the input number "n".
2. Create an empty array called "primes".
3. Use a while loop to iterate from 2 to the square root of "prime".
4. Check if "prime" is divisible by the current iteration number. If it is, divide the "prime" by the iteration number and add it to the "primes" array. Repeat this process until "prime" is no longer divisible by the current iteration number.
5. After the while loop, check if the "prime" is equal to 1. If it is, return the last element of the "primes" array, which is the largest prime factor. If it's not 1, return the "prime" itself as the largest prime factor.
6. If the input number is less than 2, return -1 as an invalid input.

Here's the code implementation:

```go
package main

import (
    "fmt"
    "math"
)

func LargestPrimeFactor(n int) int {
    if n < 2 {
        return -1
    }

    prime := n
    primes := []int{}

    i := 2
    for i <= int(math.Sqrt(float64(prime))) {
        for prime%i == 0 {
            prime /= i
            primes = append(primes, i)
        }
        i++
    }

    if prime != 1 {
        primes = append(primes, prime)
    }

    return primes[len(primes)-1]
}

func main() {
    fmt.Println(LargestPrimeFactor(13195)) // 29
    fmt.Println(LargestPrimeFactor(2048))  // 2
}
```

This code will return the largest prime factor of the input number. For example, when you pass 13195 as an argument, it will return 2