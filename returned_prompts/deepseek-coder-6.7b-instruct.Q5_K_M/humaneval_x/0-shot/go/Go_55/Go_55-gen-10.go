
    // Base Case: Fib(0) = 0, Fib(1) = 1
    if n <= 1 {
        return n
    }

    // Recursive Case: Fib(n) = Fib(n-1) + Fib(n-2)
    return Fib(n-1) + Fib(n-2)
}

func main() {
    fmt.Println(Fib(10))  // 55
    fmt.Println(Fib(1))   // 1
    fmt.Println(Fib(8))   // 21
}


// Time complexity: O(2^n)
// The space complexity: O(n) due to the function call stack.
```

The above function works, but it's not efficient as it performs a lot of redundant calculations. For larger numbers, it takes a lot of time.

A more efficient solution would be to use dynamic programming to store the results of sub-problems, so that each sub-problem is solved only once.

### Dynamic Programming Solution

```go
package main

import "fmt"

func Fib(n int) int {
    // Initialize lookup table for storing the Fibonacci numbers.
    lookup := make([]int, n+1)

    // Base case
    lookup[0] = 0
    lookup[1] = 1

    // Iteratively compute the Fibonacci numbers.
    for i := 2; i <= n; i++ {
        lookup[i] = lookup[i-1] + lookup[i-2]
    }

    return lookup[n]
}

func main() {
    fmt.Println(Fib(10))  // 55
    fmt.Println(Fib(1))   // 1
    fmt.Println(Fib(8))   // 21
}

// Time complexity: O(n)
// Space complexity: O(n)
```

The above function works efficiently for larger numbers. The time complexity is O(n) and the space complexity is also O(n). The lookup table is used to store the computed F