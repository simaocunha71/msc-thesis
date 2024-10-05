Here is a possible implementation of the `Simplify` function in Go:
```go
package main

import (
    "strconv"
    "strings"
)

func Simplify(x, n string) bool {
    numeratorX, _ := strconv.Atoi(strings.Split(x, "/")[0])
    denominatorX, _ := strconv.Atoi(strings.Split(x, "/")[1])
    numeratorN, _ := strconv.Atoi(strings.Split(n, "/")[0])
    denominatorN, _ := strconv.Atoi(strings.Split(n, "/")[1])

    numerator := numeratorX * numeratorN
    denominator := denominatorX * denominatorN

    gcd := findGCD(denominator, numerator)
    numerator /= gcd
    denominator /= gcd

    if numerator%denominator == 0 {
        return true
    }
    return false
}

func findGCD(a, b int) int {
    for b != 0 {
        a, b = b, a%b
    }
    return a
}

func main() {
    fmt.Println(Simplify("1/5", "5/1"))  // true
    fmt.Println(Simplify("1/6", "2/1"))  // false
    fmt.Println(Simplify("7/10", "10/2")) // false
}
```
This implementation first converts the input strings to integers using `strconv.Atoi` and then calculates the numerator and denominator of the resulting fraction. It then finds the greatest common divisor (GCD) of the numerator and denominator using the `findGCD` function, and simplifies the fraction by dividing both the numerator and denominator by the GCD. Finally, it checks if the simplified fraction is a whole number by checking if the remainder of the division is 0. If it is, the function returns `true`, otherwise it returns `false`.