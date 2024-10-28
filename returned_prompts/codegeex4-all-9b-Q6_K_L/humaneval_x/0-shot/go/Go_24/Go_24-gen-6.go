To find the largest number that divides `n` evenly (which is also known as the greatest common divisor, or GCD), you can use the Euclidean algorithm. This algorithm repeatedly replaces the larger number by its remainder when divided by the smaller number until one of the numbers becomes zero. The other number at this point will be the GCD. Here's how you can implement this in Go:

```go
package main

import "fmt"

// LargestDivisor finds the largest number that divides n evenly, smaller than n
func LargestDivisor(n int) int {
    if n == 1 {
        // If n is 1, the largest divisor is 1 itself
        return 1
    }

    for i := n / 2; i > 0; i-- {
        // Check if i is a divisor of n
        if n%i == 0 {
            // If i divides n evenly, return i as the largest divisor
            return i
        }
    }

    // If no divisor is found, return 1 (this case should not occur for n > 1)
    return 1
}

func main() {
    fmt.Println(LargestDivisor(15)) // Output: 5
}
```

This code starts the loop from `n/2` because a number cannot have a divisor greater than itself and smaller than half of itself. If `n` is 1, it returns 1 as the largest divisor because 1 is the only divisor of 1.