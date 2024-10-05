package main

import "fmt"

// This function takes two positive numbers x and y and returns the
// biggest even integer number that is in the range [x, y] inclusive. If
// there's no such number, then the function should return -1.
// 
// For example:
// ChooseNum(12, 15) = 14
// ChooseNum(13, 12) = -1
func ChooseNum(x, y int) int {
    if x > y {
        return -1
    }
    if x % 2 != 0 {
        x++
    }
    if x > y {
        return -1
    }
    return x
}

func main() {
    fmt.Println(ChooseNum(12, 15)) // 14
    fmt.Println(ChooseNum(13, 12)) // -1
}