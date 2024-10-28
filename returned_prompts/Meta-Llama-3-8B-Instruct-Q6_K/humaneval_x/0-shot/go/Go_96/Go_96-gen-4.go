```go
package main

import (
    "fmt"
    "math"
)

func CountUpTo(n int) []int {
    if n <= 1 {
        return []int{}
    }
    primes := []int{}
    for i := 2; i < n; i++ {
        isPrime := true
        for j := 2; j <= int(math.Sqrt(float64(i))); j++ {
            if i%j == 0 {
                isPrime = false
                break
            }
        }
        if isPrime {
            primes = append(primes, i)
        }
    }
    return primes
}

func main() {
    fmt.Println(CountUpTo(5))  // [2,3]
    fmt.Println(CountUpTo(11)) // [2,3,5,7]
    fmt.Println(CountUpTo(0))  // []
    fmt.Println(CountUpTo(20)) // [2,3,5,7,11,13,17,19]
    fmt.Println(CountUpTo(1))  // []
    fmt.Println(CountUpTo(18)) // [2,3,5,7,11,13,17]
}
```
This program defines a function `CountUpTo(n int)` that returns an array of the first n integers that are prime numbers and less than n. It uses a nested loop to check each number from 2 to n-1 whether it's prime or not. If a number is prime, it's added to the `primes` array. Finally, the `primes` array is returned. The `main` function tests the `CountUpTo` function with different inputs. The output is printed to the console.

The time complexity of this program is O(n*sqrt(n)) because for each number from 2 to n-1, we check whether it's prime or not, and the check involves a loop up to sqrt(i). The space complexity is O(n) because we store the prime numbers in an array. This program can be optimized by using a more efficient algorithm for checking primality, such as the Sieve of Eratosthenes. However, the current implementation is simple and easy to understand.