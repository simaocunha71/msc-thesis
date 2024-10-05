package main

import (
    "fmt"
)

func SameChars(s0 string, s1 string) bool {
    if len(s0) != len(s1) {
        return false
    }

    for i := 0; i < len(s0); i++ {
        if s0[i] != s1[i] {
            return false
        }
    }

    return true
}

func main() {
    fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc")) // true
    fmt.Println(SameChars("abcd", "dddddddabc"))               // true
    fmt.Println(SameChars("dddddddabc", "abcd"))               // true
    fmt.Println(SameChars("eabcd", "dddddddabc"))               // false
    fmt.Println(SameChars("abcd", "dddddddabce"))               // false
    fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddddabc"))    // false
}