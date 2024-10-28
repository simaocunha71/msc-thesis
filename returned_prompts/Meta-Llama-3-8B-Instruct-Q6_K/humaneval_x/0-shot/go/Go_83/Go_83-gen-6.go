package main

import (
    "math"
)

func StartsOneEnds(n int) int {
    if n < 1 {
        panic("n should be a positive integer")
    }
    count := 0
    for i := 1; i < math.Pow10(n); i++ {
        if i%10 == 1 || int(math.Log10(i)+1) == n {
            count++
        }
    }
    return count
}

func main() {
    n := 3
    result := StartsOneEnds(n)
    println(result)
}
