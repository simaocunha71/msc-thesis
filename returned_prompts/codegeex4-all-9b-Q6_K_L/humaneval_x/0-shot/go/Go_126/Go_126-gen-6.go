package main

import (
    "fmt"
)

func IsSorted(lst []int) bool {
    for i := 0; i < len(lst)-1; i++ {
        if lst[i] > lst[i+1] {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(IsSorted([]int{5}))
    fmt.Println(IsSorted([]int{1, 2, 3, 4, 5}))
    fmt.Println(IsSorted([]int{1, 3, 2, 4, 5}))
    fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6}))
    fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6, 7}))
    fmt.Println(IsSorted([]int{1, 3, 2, 4, 5, 6, 7}))
    fmt.Println(IsSorted([]int{1, 2, 2, 3, 3, 4}))
    fmt.Println(IsSorted([]int{1, 2, 2, 2, 3, 4}))
}

// Output:
// true
// true
// false
// true
// true
// false
// true
// false