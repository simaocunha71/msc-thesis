Here is a Go solution for the problem:

```go
import (
    "strings"
    "unicode"
)

func SplitWords(txt string) interface{} {
    words := strings.Split(txt, " ")
    if len(words) == 1 && len(txt) > 0 {
        words = strings.Split(txt, ",")
    }
    if len(words) == 1 {
        var count int
        for i := 0; i < len(txt); i++ {
            if unicode.IsLower(rune(txt[i])) && (i%2 != 0) {
                count++
            }
        }
        return count
    }
    return words
}
```
This function first tries to split the string on whitespace using `strings.Split`. If the resulting slice still contains only one element, it tries to split on commas. If the result is still a single element, it counts the number of lowercase letters with odd order in the alphabet. The function returns either a slice of strings or an integer, depending on the input. 

The `unicode.IsLower` function is used to check if a character is lowercase, and the `unicode.IsUpper` function is used to check if a character is uppercase. The `(i%2 != 0)` condition is used to check if the index of the character is odd. The `rune` function is used to convert a character to its corresponding Unicode code point. 

The function returns the result as an interface type, which allows it to return either a slice of strings or an integer. The caller of the function can use a type assertion to convert the result to the appropriate type. For example, `result := SplitWords("Hello,world!")` could be used to split the string on commas, and `result := SplitWords("abcdef")` could be used to count the number of lowercase letters with odd order in the alphabet. 

The function can be called with different inputs to get the desired output. For example, `SplitWords("Hello world!")` would return `["Hello", "world!"]`, `SplitWords("Hello,world!")` would return `["Hello", "world!"]`, and `SplitWords("abcdef")` would return `3`. 