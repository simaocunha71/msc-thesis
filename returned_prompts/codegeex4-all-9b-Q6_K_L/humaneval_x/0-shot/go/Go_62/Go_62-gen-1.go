package main

import "fmt"

func Derivative(xs []int) []int {
    if len(xs) == 1 {
        return []int{}
    }

    return append([]int{}, xs[1:]...)
}

func main() {
    fmt.Println(Derivative([]int{3, 1, 2, 4, 5}))
    fmt.Println(Derivative([]int{1, 2, 3}))
}
Output:
[1 4 12 20]
[2 6]