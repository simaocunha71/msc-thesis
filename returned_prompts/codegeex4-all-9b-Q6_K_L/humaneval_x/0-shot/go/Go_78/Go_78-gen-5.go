package main

import (
"fmt"
"strings"
)

func HexKey(num string) int {
    primeHex := map[rune]bool{'2': true, '3': true, '5': true, '7': true, 'B': true, 'D': true}
    count := 0
    for _, r := range num {
        if _, ok := primeHex[r]; ok {
            count++
        }
    }
    return count
}

func main() {
    fmt.Println(HexKey("AB"))          // 1
    fmt.Println(HexKey("1077E"))       // 2
    fmt.Println(HexKey("ABED1A33"))    // 4
    fmt.Println(HexKey("123456789ABCDEF0")) // 6
    fmt.Println(HexKey("2020"))        // 2
}

func HexKey(num string) int {
    primeHex := map[rune]bool{'2': true, '3': true, '5': true, '7': true, 'B': true, 'D': true}
    count := 0
    for _, r := range num {
        if _, ok := primeHex[r]; ok {
            count++
        }
    }
    return count
}

func main() {
    fmt.Println(HexKey("AB"))          // 1
    fmt.Println(HexKey("1077E"))       // 2
    fmt.Println(HexKey("ABED1A33"))    // 4
    fmt.Println(HexKey("123456789ABCDEF0")) // 6
    fmt.Println(HexKey("2020"))        // 2
}

func HexKey(num string) int {
    primeHex := map[rune]bool{'2': true, '3': true, '5': true, '7': true, 'B': true, 'D': true}
    count := 0
    for _, r := range num {
        if _, ok := primeHex[r]; ok {
            count++
        }
    }
    return count
}

func main() {
    fmt.Println(HexKey("AB"))          // 1
    fmt.Println(HexKey("1077E"))       // 2
    fmt.Println(HexKey("ABED1A33"))    // 4
    fmt.Println(HexKey("123456789ABCDEF0")) // 6
    fmt.Println(Hex