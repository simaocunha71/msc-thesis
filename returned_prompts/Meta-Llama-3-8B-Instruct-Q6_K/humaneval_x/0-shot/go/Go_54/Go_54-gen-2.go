```go
package main

import (
    "fmt"
    "sort"
)

func SameChars(s0 string, s1 string) bool {
    if len(s0) != len(s1) {
        return false
    }
    count0 := make([]int, 256)
    count1 := make([]int, 256)
    for _, c := range s0 {
        count0[c]++
    }
    for _, c := range s1 {
        count1[c]++
    }
    for i := 0; i < 256; i++ {
        if count0[i] != count1[i] {
            return false
        }
    }
    return true
}

func main() {
    fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddeddabc")) // true
    fmt.Println(SameChars("abcd", "dddddddabc")) // true
    fmt.Println(SameChars("dddddddabc", "abcd")) // true
    fmt.Println(SameChars("eabcd", "dddddddabc")) // false
    fmt.Println(SameChars("abcd", "dddddddabce")) // false
    fmt.Println(SameChars("eabcdzzzz", "dddzzzzzzzddddabc")) // false
}
```


The problem is asking to write a function that checks if two strings have the same characters, regardless of their order and frequency. For example, the strings "eabcdzzzz" and "dddzzzzzzzddeddabc" have the same characters, while the strings "eabcd" and "dddddddabc" do not.

Here is a Go solution that uses two arrays to count the occurrences of each character in the two strings, and then compares the counts:

```go
func SameChars(s0 string, s1 string) bool {
    if len(s0) != len(s1) {
        return false
    }
    count0 := make([]int, 256)
    count1 := make([]int, 256)
    for _, c := range s0 {
        count0[c]++
    }
    for _, c := range s1 {
        count1[c]++
    }
    for i := 0; i < 256; i++ {
        if count0[i] != count1[i] {
            return false
        }
    }
    return true
}
```

This function works by first checking if the two strings have the same length.