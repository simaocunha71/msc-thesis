Here is the solution in Go:

```go
package main

import (
    "sort"
    "strings"
)

func AntiShuffle(s string) string {
    words := strings.Fields(s)
    result := make([]string, len(words))
    for i, word := range words {
        bytes := []byte(word)
        sort.Slice(bytes, func(i, j int) bool {
            return bytes[i] < bytes[j]
        })
        result[i] = string(bytes)
    }
    return strings.Join(result, " ")
}

func main() {
    fmt.Println(AntiShuffle("Hi"))  // Output: "Hi"
    fmt.Println(AntiShuffle("hello"))  // Output: "ehllo"
    fmt.Println(AntiShuffle("Hello World!!!"))  // Output: "Hello !!!Wdlor"
}
```

This program works by splitting the input string into words, then for each word, it sorts the bytes of the word in ascending order. The sorted bytes are then converted back to a string. Finally, the sorted words are joined back together with spaces in between to form the final result. The `sort.Slice` function is used to sort the bytes in ascending order. The `strings.Fields` function is used to split the input string into words, and the `strings.Join` function is used to join the sorted words back together. The `main` function is used to test the `AntiShuffle` function with different input strings. 