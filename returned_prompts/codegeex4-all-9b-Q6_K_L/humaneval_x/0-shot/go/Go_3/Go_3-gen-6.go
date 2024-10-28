package main

import "fmt"

func BelowZero(operations []int) bool {
    balance := 0
    for _, operation := range operations {
        balance += operation
        if balance < 0 {
            return true
        }
    }
    return false
}

func main() {
    fmt.Println(BelowZero([]int{1, 2, 3})) // false
    fmt.Println(BelowZero([]int{1, 2, -4, 5})) // true
}