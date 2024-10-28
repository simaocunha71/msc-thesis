package main

import (
    "fmt"
    "strings"
)

func Solve(s string) string {
    if !strings.ContainsAny(s, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return reverse(s)
    }
    var result string
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result += string(c - 'a' + 'A')
        } else if c >= 'A' && c <= 'Z' {
            result += string(c - 'A' + 'a')
        } else {
            result += string(c)
        }
    }
    return result
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}

func main() {
    fmt.Println(Solve("1234")) // "4321"
    fmt.Println(Solve("ab"))   // "AB"
    fmt.Println(Solve("#a@C")) // "#A@c"
}

```go
func Solve(s string) string {
    if !strings.ContainsAny(s, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        return reverse(s)
    }
    var result string
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result += string(c - 'a' + 'A')
        } else if c >= 'A' && c <= 'Z' {
            result += string(c - 'A' + 'a')
        } else {
            result += string(c)
        }
    }
    return result
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```