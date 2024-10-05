package main

import (
    "fmt"
    "math"
)

func PrimeLength(s string) bool {
    length := len(s)
    if length < 2 {
        return false
    }
    for i := 2; i <= int(math.Sqrt(float64(length))); i++ {
        if length%i == 0 {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(PrimeLength("Hello"))
    fmt.Println(PrimeLength("abcdcba"))
    fmt.Println(PrimeLength("kittens"))
    fmt.Println(PrimeLength("orange"))
}