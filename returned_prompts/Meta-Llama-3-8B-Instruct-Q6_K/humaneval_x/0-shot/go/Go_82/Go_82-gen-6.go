```
package main

import (
    "fmt"
)

func PrimeLength(s string) bool {
    length := len(s)
    if length <= 1 {
        return false
    }
    for i := 2; i <= length/2; i++ {
        if length%i == 0 {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(PrimeLength("Hello")) // true
    fmt.Println(PrimeLength("abcdcba")) // true
    fmt.Println(PrimeLength("kittens")) // true
    fmt.Println(PrimeLength("orange")) // false
}
```

This function `PrimeLength` takes a string `s` as input, calculates its length `length`, and then checks if it is a prime number. It does this by iterating from 2 to `length/2` and checking if `length` is divisible by any of these numbers. If it is, it returns `false`, indicating that the string length is not prime. If it is not divisible by any of these numbers, it returns `true`, indicating that the string length is prime.

In the `main` function, we test the `PrimeLength` function with the provided examples, and the output is as expected. The string lengths "Hello", "abcdcba", and "kittens" are all prime numbers, so the function returns `true` for each of these. The string length "orange" is not a prime number, so the function returns `false` for this one.