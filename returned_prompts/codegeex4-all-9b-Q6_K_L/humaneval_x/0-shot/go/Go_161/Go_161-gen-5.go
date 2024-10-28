package main

import (
    "fmt"
    "strings"
)

func Solve(s string) string {
    for i := range s {
        if strings.ContainsRune("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ", rune(s[i])) {
            if 'a' <= s[i] && s[i] <= 'z' {
                s = strings.Replace(s, string(s[i]), strings.ToUpper(string(s[i])), 1)
            } else {
                s = strings.Replace(s, string(s[i]), strings.ToLower(string(s[i])), 1)
            }
        }
    }
    if !strings.ContainsAny(s, "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") {
        s = reverse(s)
    }
    return s
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