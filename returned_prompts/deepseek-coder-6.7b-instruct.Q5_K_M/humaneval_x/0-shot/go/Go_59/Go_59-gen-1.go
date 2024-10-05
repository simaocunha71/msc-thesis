
// Create a variable to store the largest prime factor
    var largestPrimeFactor int

B:

    // Start from 2 and go up to the square root of n
    for i := 2; i*i <= n; i++ {
        // If n is divisible by i, then i is a factor
        if n % i == 0 {
            // Divide n by i to get the new n
            n = n / i
            // Set i as the largest prime factor
            largestPrimeFactor = i
            // Continue the loop to find the largest prime factor
            goto B
        }
    }

    // If n is greater than 1, then n is the largest prime factor
    if n > 1 {
        largestPrimeFactor = n
    }

    return largestPrimeFactor
}


```

Here, the algorithm starts by dividing the input number by 2, and checks if it's divisible. If it is, it sets the divisor as the largest prime factor and continues with the division of the result. If it's not, it increments the divisor by 1 and continues the process. This continues until the divisor is greater than the square root of the input number. If the result of the division is greater than 1, it means that the result is a prime number and is the largest prime factor of the input.

This algorithm has a time complexity of O(sqrt(n)) because in the worst case it needs to go up to the square root of the input number. It also has a space complexity of O(1) because it uses a constant amount of space.

This implementation is written in Go language.

Note: This implementation does not handle the cases when the input number is less than or equal to 1, because such cases are not considered valid inputs for this problem.

```go
package main

import (
	"fmt"
)

func LargestPrimeFactor(n int) int {
	var largestPrimeFactor int
	for i := 2; i*i <= n; i++ {
		if n % i == 0 {
			n = n / i
			largestPrimeFactor = i
			goto B
		}
	}