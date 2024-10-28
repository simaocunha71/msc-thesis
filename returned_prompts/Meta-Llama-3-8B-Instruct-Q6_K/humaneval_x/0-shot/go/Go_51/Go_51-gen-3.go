Here is the solution:

```go
import (
    "regexp"
)

// RemoveVowels is a function that takes string and returns string without vowels.
func RemoveVowels(text string) string {
    // Create a regular expression that matches all vowels
    re := regexp.MustCompile(`[aeiouAEIOU]`)
    // Replace all vowels with an empty string
    return re.ReplaceAllString(text, "")
}
```



Explanation:
The RemoveVowels function uses the `regexp` package to create a regular expression that matches all vowels (both lowercase and uppercase). The `ReplaceAllString` function is then used to replace all occurrences of the vowels with an empty string, effectively removing them from the input text. The result is a new string that contains all characters from the input text except for the vowels.