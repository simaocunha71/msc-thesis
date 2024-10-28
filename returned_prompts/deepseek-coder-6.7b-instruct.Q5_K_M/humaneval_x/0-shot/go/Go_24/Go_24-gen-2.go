
    for i := n - 1; i > 0; i-- {
        if n%i == 0 {
            return i
        }
    }
    return -1
}

```

The function `LargestDivisor(n int) int` takes an integer `n` as input and returns the largest number that divides `n` evenly, smaller than `n`.

In the function, we start from `n-1` and decrement down to 1. If `n` modulo `i` is 0, we return `i` because `i` is the largest number that divides `n` evenly. If no such `i` is found, the function returns -1.

This solution is not efficient for large numbers since it checks each number in descending order. For a more efficient solution, one could use a prime factorization method to find the largest divisor. However, this solution is sufficient for small inputs.

```go

package main

import (
    "fmt"
)

func main() {
    fmt.Println(LargestDivisor(15)) // 5
}

```

In the main function, we test `LargestDivisor(15)` which should return 5.

This program should print `5`.

This program finds the largest divisor of a number `n` by iterating from `n-1` to `1` and checking if `n` is divisible by the current number `i`. If it is, `i` is the largest divisor of `n`.

This program is written in Go, which is a statically typed, compiled programming language designed at Google. It is syntactically similar to C, but with memory safety, garbage collection, structural typing, and CSP-style concurrency.

```go

package main

import (
    "fmt"
)

func main() {
    fmt.Println(LargestDivisor(15)) // 5
}

```

In the main function, we test `LargestDivisor(15)` which should return 5.

This program should print `5`.

This program finds the largest divisor of a number `