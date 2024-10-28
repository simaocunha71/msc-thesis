Here is a Go function that simplifies the expression x * n and checks if the result is a whole number:
```go
package main

import (
    "strconv"
    "strings"
)

func Simplify(x, n string) bool {
    // Parse the fractions
    xNum, _ := strconv.Atoi(strings.Split(x, "/")[0])
    xDen, _ := strconv.Atoi(strings.Split(x, "/")[1])
    nNum, _ := strconv.Atoi(strings.Split(n, "/")[0])
    nDen, _ := strconv.Atoi(strings.Split(n, "/")[1])

    // Calculate the product
    prodNum := xNum * nNum
    prodDen := xDen * nDen

    // Check if the product is a whole number
    if prodDen == 1 {
        return true
    }
    if gcd(prodNum, prodDen) == 1 {
        return true
    }
    return false
}

// Calculate the greatest common divisor (GCD) of two numbers
func gcd(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

func main() {
    // Test the function
    fmt.Println(Simplify("1/5", "5/1")) // Output: true
    fmt.Println(Simplify("1/6", "2/1")) // Output: false
    fmt.Println(Simplify("7/10", "10/2")) // Output: false
}
```
The `Simplify` function parses the input fractions, calculates the product, and then checks if the product is a whole number by checking if the denominator is 1 or if the GCD of the numerator and denominator is 1. The `gcd` function is used to calculate the GCD of two numbers. In the `main` function, we test the `Simplify` function with some sample inputs.