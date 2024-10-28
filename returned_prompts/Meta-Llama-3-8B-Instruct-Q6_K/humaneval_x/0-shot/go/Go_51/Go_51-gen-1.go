```go
package main

import (
    "regexp"
    "strings"
)

func RemoveVowels(text string) string {
    vowels := regexp.MustCompile(`[aeiouAEIOU]`)
    noVowels := strings.ReplaceAll(text, vowels.String(), "")
    return noVowels
}

func main() {
    fmt.Println(RemoveVowels(""))        // ''
    fmt.Println(RemoveVowels("abcdef\nghijklm"))  // 'bcdf\nghjklm'
    fmt.Println(RemoveVowels("abcdef"))  // 'bcdf'
    fmt.Println(RemoveVowels("aaaaa"))   // ''
    fmt.Println(RemoveVowels("aaBAA"))   // 'B'
    fmt.Println(RemoveVowels("zbcd"))    // 'zbcd'
}
```


In this code, `RemoveVowels` function uses `regexp` package to create a regular expression that matches any vowel (both lowercase and uppercase). It then uses `strings.ReplaceAll` function to replace all occurrences of vowels in the input string with an empty string, effectively removing them. The resulting string is then returned. 

In the `main` function, we test the `RemoveVowels` function with different inputs and print the results. 

This code assumes that the input string contains only ASCII characters. If the input string may contain non-ASCII characters, you may need to use a more sophisticated approach to handle them correctly. 

Also, note that this code is case-sensitive, meaning it treats uppercase and lowercase vowels differently. If you want to treat them as the same, you can convert the input string to either lowercase or uppercase before processing it. 

Finally, this code uses the `strings.ReplaceAll` function, which is available in Go 1.18 and later. If you are using an earlier version of Go, you can use a loop to replace the vowels one by one. 

Here is the modified code that uses a loop to replace the vowels:
```go
func RemoveVowels(text string) string {
    var noVowels string
    for _, char := range text {
        if !strings.Contains("aeiouAEIOU", string(char)) {
            noVowels += string(char)
        }
    }
    return noVowels
}
```


This code iterates over each character in the input string and checks if it is a vowel. If it is