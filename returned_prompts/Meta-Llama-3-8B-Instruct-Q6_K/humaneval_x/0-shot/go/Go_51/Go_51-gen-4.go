Here is the solution to the problem:
```go
package main

import (
    "regexp"
)

func RemoveVowels(text string) string {
    // Create a regular expression that matches any vowel (both lowercase and uppercase)
    re := regexp.MustCompile(`[aeiouAEIOU]`)

    // Use the ReplaceAllString function to replace all vowels with an empty string
    result := re.ReplaceAllString(text, "")

    return result
}

func main() {
    // Test cases
    println(RemoveVowels(""))    // ''
    println(RemoveVowels("abcdef\nghijklm"))  // 'bcdf\nghjklm'
    println(RemoveVowels("abcdef"))   // 'bcdf'
    println(RemoveVowels("aaaaa"))    // ''
    println(RemoveVowels("aaBAA"))    // 'B'
    println(RemoveVowels("zbcd"))     // 'zbcd'
}
```
In this solution, we use the `regexp` package to create a regular expression that matches any vowel (both lowercase and uppercase). We then use the `ReplaceAllString` function to replace all vowels in the input text with an empty string, effectively removing them. The resulting string is then returned. The `main` function is used to test the `RemoveVowels` function with different input strings.