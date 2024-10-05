```go
package main

import (
    "fmt"
    "strings"
)

func Histogram(test string) map[rune]int {
    if test == "" {
        return make(map[rune]int)
    }
    words := strings.Split(test, " ")
    counts := make(map[rune]int)
    for _, word := range words {
        for _, r := range word {
            counts[r]++
        }
    }
    maxCount := 0
    result := make(map[rune]int)
    for k, v := range counts {
        if v > maxCount {
            maxCount = v
            result = make(map[rune]int)
            result[k] = v
        } else if v == maxCount {
            result[k] = v
        }
    }
    return result
}

func main() {
    fmt.Println(Histogram("a b c"))  // map[rune]int{'a':1, 'b':1, 'c':1}
    fmt.Println(Histogram("a b b a")) // map[rune]int{'a':2, 'b':2}
    fmt.Println(Histogram("a b c a b")) // map[rune]int{'a':2, 'b':2}
    fmt.Println(Histogram("b b b b a")) // map[rune]int{'b':4}
    fmt.Println(Histogram(""))  // map[rune]int{}
}
```

Explanation:
The function Histogram takes a string as input, splits it into words using the space character as a delimiter, and then for each word, it counts the occurrences of each letter. It keeps track of the maximum count and the corresponding letters, and finally returns a map of these letters with their counts.

In the main function, we test the Histogram function with different inputs and print the results. The output shows that the function correctly returns the letter(s) with the most repetition and their count(s). If there are multiple letters with the same maximum count, they are all included in the result. If the input string is empty, the function returns an empty map.