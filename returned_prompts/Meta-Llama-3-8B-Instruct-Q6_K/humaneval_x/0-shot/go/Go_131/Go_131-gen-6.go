package main

import (
    "strconv"
)

func Digits(n int) int {
    var product int
    for n > 0 {
        digit, _ := strconv.Atoi(strconv.Itoa(n % 10))
        if digit % 2 != 0 {
            product *= digit
        }
        n /= 10
    }
    return product
}

func main() {
    println(Digits(1))  // 1
    println(Digits(4))  // 0
    println(Digits(235)) // 15
}