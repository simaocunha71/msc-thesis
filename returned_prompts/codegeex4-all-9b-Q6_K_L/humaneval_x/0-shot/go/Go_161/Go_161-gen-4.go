package main

import "fmt"

func Solve(s string) string {
    var result string
    for i := 0; i < len(s); i++ {
        if s[i] >= 'a' && s[i] <= 'z' {
            result += string(s[i] - 32)
        } else if s[i] >= 'A' && s[i] <= 'Z' {
            result += string(s[i] + 32)
        } else {
            result += string(s[i])
        }
    }
    return result
}

func main() {
    fmt.Println(Solve("1234")) // "4321"
    fmt.Println(Solve("ab"))   // "AB"
    fmt.Println(Solve("#a@C")) // "#A@c"
}