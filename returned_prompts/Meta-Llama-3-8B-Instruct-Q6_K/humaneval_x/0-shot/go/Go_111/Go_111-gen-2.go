```go
package main

import (
    "strings"
    "fmt"
)

func Histogram(test string) map[rune]int {
    if test == "" {
        return map[rune]int{}
    }
    words := strings.Split(test, " ")
    charCount := make(map[rune]int)
    for _, word := range words {
        for _, char := range word {
            charCount[char]++
        }
    }
    maxCount := 0
    var result map[rune]int
    for char, count := range charCount {
        if count > maxCount {
            maxCount = count
            result = map[rune]int{char: count}
        } else if count == maxCount {
            result[charCount[char]] = count
        }
    }
    return result
}

func main() {
    fmt.Println(Histogram("a b c")) // {"a": 1, "b": 1, "c": 1}
    fmt.Println(Histogram("a b b a")) // {"a": 2, "b": 2}
    fmt.Println(Histogram("a b c a b")) // {"a": 2, "b": 2}
    fmt.Println(Histogram("b b b b a")) // {"b": 4}
    fmt.Println(Histogram("")) // {}
}
```

















