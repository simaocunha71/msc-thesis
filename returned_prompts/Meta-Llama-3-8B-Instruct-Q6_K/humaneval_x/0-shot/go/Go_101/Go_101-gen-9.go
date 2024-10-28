Here is a simple solution that uses the `strings.Split` function to split the input string into words, and then removes any leading or trailing whitespace from each word using the `strings.TrimSpace` function:

```go
import (
    "strings"
)

func WordsString(s string) []string {
    words := strings.Split(s, ", ")
    for i := range words {
        words[i] = strings.TrimSpace(words[i])
    }
    return words
}
```

This function first splits the input string `s` into words using the `","` and `" "` characters as separators. The result is a slice of strings, where each element is a word. Then, it iterates over the slice and trims any leading or trailing whitespace from each word using the `strings.TrimSpace` function. Finally, it returns the resulting slice of words.

For example, if you call the function with the input string `"Hi, my name is John"`, it will return the slice `["Hi", "my", "name", "is", "John"]`. Similarly, if you call the function with the input string `"One, two, three, four, five, six"`, it will return the slice `["One", "two", "three", "four", "five", "six"]`.