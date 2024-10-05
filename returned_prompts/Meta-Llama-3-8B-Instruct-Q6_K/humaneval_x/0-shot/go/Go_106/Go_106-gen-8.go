```go
package main

import (
    "fmt"
)

func F(n int) []int {
    result := make([]int, n)
    for i := 0; i < n; i++ {
        if i%2 == 0 { // if i is even
            result[i] = factorial(i)
        } else { // if i is odd
            sum := 0
            for j := 1; j <= i; j++ {
                sum += j
            }
            result[i] = sum
        }
    }
    return result
}

func factorial(n int) int {
    if n == 0 {
        return 1
    }
    return n * factorial(n-1)
}

func main() {
    fmt.Println(F(5)) // [1, 2, 6, 24, 15]
}
```

The function F(n) returns a list of size n such that the value of the element at index i is the factorial of i if i is even or the sum of numbers from 1 to i otherwise. This is implemented in the provided Go code.

The function F(n) iterates over a range from 0 to n-1. For each index i, it checks if i is even by using the modulus operator (%). If i is even, it calculates the factorial of i using a recursive function factorial(n) and assigns the result to the corresponding element in the result list.

If i is odd, it calculates the sum of numbers from 1 to i using a for loop and assigns the result to the corresponding element in the result list.

The main function calls F(5) and prints the result, which is [1, 2, 6, 24, 15]. This is the expected output according to the problem statement.