```go
package main

import (
    "fmt"
    "sort"
)

func FindMax(words []string) string {
    max := ""
    maxCount := 0
    for _, word := range words {
        count := len(set([]rune(word)))
        if count > maxCount {
            max = word
            maxCount = count
        } else if count == maxCount {
            if word < max {
                max = word
            }
        }
    }
    return max
}

func set(runes []rune) []rune {
    seen := make(map[rune]bool)
    result := []rune{}
    for _, val := range runes {
        if seen[val] {
            continue
        }
        seen[val] = true
        result = append(result, val)
    }
    sort.Slice(result, func(i, j int) bool {
        return result[i] < result[j]
    })
    return result
}

func main() {
    fmt.Println(FindMax([]string{"name", "of", "string"}))  // "string"
    fmt.Println(FindMax([]string{"name", "enam", "game"})) // "enam"
    fmt.Println(FindMax([]string{"aaaaaaa", "bb", "cc"}))  // "aaaaaaa"
}
```

Explanation:
The function `FindMax` iterates over each word in the list, counts the number of unique characters, and keeps track of the maximum count and the corresponding word. If multiple words have the maximum count, it returns the one which comes first in lexicographical order.

The function `set` is used to remove duplicates from a slice of runes and sorts the resulting slice in lexicographical order. This is used to count the number of unique characters in a word.

The function `main` tests the `FindMax` function with different inputs.