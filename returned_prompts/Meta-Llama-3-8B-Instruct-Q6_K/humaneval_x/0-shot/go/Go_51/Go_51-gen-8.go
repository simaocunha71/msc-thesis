Here is a simple function in Go that removes all the vowels from a given string:

```go
package main

import (
    "regexp"
    "strings"
)

func RemoveVowels(text string) string {
    vowels := "aeiouAEIOU"
    for _, v := range vowels {
        text = strings.ReplaceAll(text, string(v), "")
    }
    return text
}

func main() {
    fmt.Println(RemoveVowels("")) // ''
    fmt.Println(RemoveVowels("abcdef\nghijklm")) // 'bcdf\nghjklm'
    fmt.Println(RemoveVowels("abcdef")) // 'bcdf'
    fmt.Println(RemoveVowels("aaaaa")) // ''
    fmt.Println(RemoveVowels("aaBAA")) // 'B'
    fmt.Println(RemoveVowels("zbcd")) // 'zbcd'
}
```
This function loops over all the vowels and removes them from the text. It uses the `strings.ReplaceAll` function from Go's standard library to replace all occurrences of a vowel with an empty string, effectively removing it. The function then returns the modified text. The `main` function demonstrates how to use this function with different inputs. The output will be the text with all vowels removed. 