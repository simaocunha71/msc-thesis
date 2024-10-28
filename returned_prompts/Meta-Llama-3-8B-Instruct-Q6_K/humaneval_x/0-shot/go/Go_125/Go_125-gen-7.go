Here is a possible solution in Go:
```go
package main

import (
    "fmt"
    "strings"
)

func SplitWords(txt string) interface{} {
    words := strings.Split(txt, " ")
    if len(words) == 1 && len(txt) > 0 {
        words = strings.Split(txt, ",")
    }
    if len(words) == 1 && len(words[0]) > 0 {
        oddCount := 0
        for i := 0; i < len(words[0]); i++ {
            if strings.ToLower(string(words[0][i])) >= "a" && strings.ToLower(string(words[0][i])) <= "z" {
                if int(strings.ToLower(string(words[0][i]))-'a')%2 != 0 {
                    oddCount++
                }
            }
        }
        return oddCount
    }
    return words
}

func main() {
    fmt.Println(SplitWords("Hello world!")) // Output: ["Hello", "world!"]
    fmt.Println(SplitWords("Hello,world!")) // Output: ["Hello", "world!"]
    fmt.Println(SplitWords("abcdef")) // Output: 3
}
```
This function first tries to split the input string on whitespace using `strings.Split`. If this results in a single element, it then tries to split on commas. If this also results in a single element, it counts the number of lowercase letters with odd order in the alphabet. The result is returned as an interface{} type, which can be a slice of strings or an integer. In the main function, we test this function with the provided examples.