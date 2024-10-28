package main

import "fmt"

func HexKey(num string) int {
    var count int = 0
    for i := 0; i < len(num); i++ {
        if num[i] == '2' || num[i] == '3' || num[i] == '5' || num[i] == '7' || num[i] == 'B' || num[i] == 'D' {
            count++
        }
    }
    return count
}

func main() {
    fmt.Println(HexKey("AB")) //1
    fmt.Println(HexKey("1077E")) //2
    fmt.Println(HexKey("ABED1A33")) //4
    fmt.Println(HexKey("123456789ABCDEF0")) //6
    fmt.Println(HexKey("2020")) //2
}
