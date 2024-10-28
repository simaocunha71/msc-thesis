Here is the solution in Go:

```go
package main

import (
    "strings"
    "unicode"
)

func SplitWords(txt string) interface{} {
    words := strings.Split(txt, " ")
    if len(words) == 1 && strings.Count(txt, ",") == 0 {
        var count int
        for i := 0; i < len(txt); i++ {
            if unicode.IsLower(rune(txt[i])) && (i % 2 != 0) {
                count++
            }
        }
        return count
    }
    return words
}

func main() {
    txt := "Hello,world!"
    result := SplitWords(txt)
    if resultType, ok := result.(interface{}); ok {
        if resultType, ok := resultType.([]string); ok {
            for _, word := range resultType {
                print(word, " ")
            }
            println()
        } else {
            println(resultType)
        }
    }
}
```

In this solution, we use the `strings.Split` function to split the input string into words based on whitespace. If the input string contains only one word and no commas, we iterate over the characters in the string and count the number of lowercase letters with odd indices in the alphabet. We use the `unicode.IsLower` function to check if a character is lowercase and the modulo operator (`%`) to check if the index is odd. The result is returned as an interface{} type. In the `main` function, we demonstrate how to call the `SplitWords` function and print the result. If the result is a slice of strings, we print each word followed by a space. If the result is an integer, we simply print it.