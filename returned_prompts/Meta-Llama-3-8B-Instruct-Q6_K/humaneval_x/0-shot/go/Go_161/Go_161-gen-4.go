// Convert the string into a byte slice
b := []byte(s)

// Iterate over each byte in the byte slice
for i := 0; i < len(b); i++ {
    // Check if the byte is an ASCII letter
    if b[i] >= 'a' && b[i] <= 'z' || b[i] >= 'A' && b[i] <= 'Z' {
        // If it's lowercase, convert it to uppercase
        if b[i] >= 'a' && b[i] <= 'z' {
            b[i] = b[i] - 32
        }
        // If it's uppercase, convert it to lowercase
        else {
            b[i] = b[i] + 32
        }
    }
}
// If the string contains no letters, reverse the string
if !containsLetters(b) {
    reverseBytes(b)
}

// Convert the byte slice back into a string
return string(b)
}

// Helper function to check if a byte slice contains letters
func containsLetters(b []byte) bool {
    for _, v := range b {
        if v >= 'a' && v <= 'z' || v >= 'A' && v <= 'Z' {
            return true
        }
    }
    return false
}

// Helper function to reverse a byte slice
func reverseBytes(b []byte) {
    start := 0
    end := len(b) - 1
    for start < end {
        b[start], b[end] = b[end], b[start]
        start++
        end--
    }
}

B:
package main

import (
    "fmt"
    "strings"
)

func Solve(s string) string {
    var result strings.Builder
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            result.WriteByte(byte(c - 'a' + 'A'))
        } else if c >= 'A' && c <= 'Z' {
            result.WriteByte(byte(c - 'A' + 'a'))
        } else {
            result.WriteByte(c)
        }
    }
    if result.String() == s {
        result.Reset()
        result.WriteString(s)
        result.Bytes()[0], result.Bytes()[len(s)-1] = result.Bytes()[len(s)-1], result.Bytes()[0]
    }
    return result.String()
}

func main() {
    fmt.Println(Solve("1234")) // 4321
    fmt.Println(Solve