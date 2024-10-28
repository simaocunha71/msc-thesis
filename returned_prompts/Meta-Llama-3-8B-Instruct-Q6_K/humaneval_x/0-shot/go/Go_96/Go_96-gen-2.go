```go
package main

import (
    "fmt"
)

func isPrime(num int) bool {
    if num <= 1 {
        return false
    }
    for i := 2; i*i <= num; i++ {
        if num%i == 0 {
            return false
        }
    }
    return true
}

func CountUpTo(n int) []int {
    result := make([]int, 0)
    for i := 2; i < n; i++ {
        if isPrime(i) {
            result = append(result, i)
        }
    }
    return result
}

func main() {
    fmt.Println(CountUpTo(5))  // [2 3]
    fmt.Println(CountUpTo(11)) // [2 3 5 7]
    fmt.Println(CountUpTo(0))  // []
    fmt.Println(CountUpTo(20)) // [2 3 5 7 11 13 17 19]
    fmt.Println(CountUpTo(1))  // []
    fmt.Println(CountUpTo(18)) // [2 3 5 7 11 13 17]
}
```


The `CountUpTo` function iterates from 2 to `n-1` and checks if each number is prime using the `isPrime` function. If the number is prime, it is appended to the result slice. Finally, the result slice is returned. The `isPrime` function checks if a number is prime by iterating from 2 to the square root of the number and checking if the number is divisible by any of these values. If the number is not divisible, it is considered prime. The `main` function tests the `CountUpTo` function with different inputs.