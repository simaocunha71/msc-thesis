package main

import (
    "fmt"
)

func Tri(n int) []float64 {
    if n == 0 {
        return []float64{3}
    }

    res := []float64{3}
    for i := 1; i <= n; i++ {
        if i%2 == 0 {
            res = append(res, 1+float64(i)/2)
        } else {
            res = append(res, res[i-1]+res[i-2]+res[i-3])
        }
    }

    return res
}

func main() {
    fmt.Println(Tri(3)) // [1 3 2 8]
    fmt.Println(Tri(5)) // [1 3 2 8 4 16]
}
