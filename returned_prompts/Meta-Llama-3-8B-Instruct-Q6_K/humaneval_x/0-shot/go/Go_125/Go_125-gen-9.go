Here is the solution in Go:

```go
package main

import (
    "fmt"
    "strings"
)

func SplitWords(txt string) interface{} {
    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    } else if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    } else {
        var count int
        for i := 0; i < len(txt); i++ {
            if 'a' <= txt[i] && txt[i] <= 'z' && (i+1)%2 == 1 {
                count++
            }
        }
        return count
    }
}

func main() {
    fmt.Println(SplitWords("Hello world!")) // Output: [Hello world!]
    fmt.Println(SplitWords("Hello,world!")) // Output: [Hello world!]
    fmt.Println(SplitWords("abcdef")) // Output: 3
}
```

This program defines a function `SplitWords` that takes a string as input and returns an interface value. If the input string contains a space, it splits the string on whitespace using the `strings.Split` function and returns the resulting slice. If the string contains a comma, it also splits the string on commas and returns the resulting slice. If the string does not contain any whitespace or commas, it counts the number of lowercase letters with odd order in the alphabet (i.e., the letters 'a', 'c', 'e', etc.) and returns this count as an integer. The `main` function demonstrates the usage of the `SplitWords` function with different input strings.