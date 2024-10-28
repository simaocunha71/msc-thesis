package main

import (
    "fmt"
    "strconv"
)

func HexKey(num string) int {
    var n int
    for _, v := range num {
        switch v {
        case '2', '3', '5', '7', 'B', 'D':
            n++
        }
    }
    return n
}

func main() {
    fmt.Println(HexKey("AB"))          // 1
    fmt.Println(HexKey("1077E"))       // 2
    fmt.Println(HexKey("ABED1A33"))    // 4
    fmt.Println(HexKey("123456789ABCDEF0")) // 6
    fmt.Println(HexKey("2020"))        // 2
}
