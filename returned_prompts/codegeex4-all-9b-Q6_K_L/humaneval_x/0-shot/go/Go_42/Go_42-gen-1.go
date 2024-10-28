package main

import "fmt"

func IncrList(l []int) []int {
    for i := 0; i < len(l); i++ {
        l[i]++
    }
    return l
}

func main() {
    fmt.Println(IncrList([]int{1, 2, 3}))
    fmt.Println(IncrList([]int{5, 3, 5, 2, 3, 3, 9, 0, 123}))
}

This solution loops through the slice and increments each element by 1.

The main function is for testing the solution.