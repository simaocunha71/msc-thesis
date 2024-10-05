Here is the solution:
```go
import (
    "regexp"
)

func RemoveVowels(text string) string {
    // Create a regular expression pattern that matches any vowel
    pattern := regexp.MustCompile(`[aeiouAEIOU]`)
    // Use the ReplaceAllString function to replace all vowels with an empty string
    return pattern.ReplaceAllString(text, "")
}
```
Explanation:

* We import the `regexp` package, which provides regular expression functionality in Go.
* We define a regular expression pattern `pattern` that matches any vowel (both lowercase and uppercase) using the character class `[aeiouAEIOU]`.
* We use the `ReplaceAllString` function to replace all occurrences of vowels in the input `text` with an empty string. This effectively removes all vowels from the input string.
* The resulting string without vowels is returned as the output of the `RemoveVowels` function.