Here is a Go function that implements the described behavior:

```go
package main

import (
    "fmt"
    "strings"
)

// Given a string of words, return a list of words split on whitespace, if no whitespaces exists in the text you
// should split on commas ',' if no commas exists you should return the number of lower-case letters with odd order in the
// alphabet, ord('a') = 0, ord('b') = 1, ... ord('z') = 25
// Examples
// SplitWords("Hello world!") ➞ ["Hello", "world!"]
// SplitWords("Hello,world!") ➞ ["Hello", "world!"]
// SplitWords("abcdef") == 3
func SplitWords(txt string) interface{} {
    words := strings.Split(txt, " ")
    if len(words) == 1 && !strings.Contains(txt, " ") {
        words = strings.Split(txt, ",")
        if len(words) == 1 && !strings.Contains(txt, ",") {
            result := 0
            for i := 0; i < len(txt); i++ {
                if txt[i] >= 'a' && txt[i] <= 'z' && i%2 != 0 {
                    result++
                }
            }
            return result
        }
    }
    return words
}

func main() {
    fmt.Println(SplitWords("Hello world!"))  // Output: [Hello world!]
    fmt.Println(SplitWords("Hello,world!")) // Output: [Hello world!]
    fmt.Println(SplitWords("abcdef"))      // Output: 3
}
```

This function uses the `strings.Split` function to split the input string into words based on whitespace or commas. If the input string does not contain any whitespace or commas, it counts the number of lowercase letters with odd order in the alphabet. The function returns an interface{} type, which can be a slice of strings or an integer. The main function demonstrates the usage of the `SplitWords` function with the given examples.