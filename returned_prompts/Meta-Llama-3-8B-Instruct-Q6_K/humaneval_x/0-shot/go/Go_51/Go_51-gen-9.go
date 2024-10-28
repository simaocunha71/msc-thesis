Here is the solution:

```go
import (
    "regexp"
)

func RemoveVowels(text string) string {
    // Create a regular expression pattern that matches any vowel.
    pattern := regexp.MustCompile(`[aeiouAEIOU]`)
    // Use the ReplaceAllString function to replace all vowels with an empty string.
    result := pattern.ReplaceAllString(text, "")
    return result
}
```

In this solution, we use the `regexp` package to create a regular expression pattern that matches any vowel (both lowercase and uppercase). We then use the `ReplaceAllString` function to replace all occurrences of vowels in the input string with an empty string, effectively removing them. The result is a new string with all vowels removed.