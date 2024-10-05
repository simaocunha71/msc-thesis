Here is a possible solution in Go:

```go
import (
    "regexp"
    "strings"
)

// RemoveVowels is a function that takes string and returns string without vowels.
func RemoveVowels(text string) string {
    vowels := regexp.MustCompile("[aeiouAEIOU]")
    return vowels.ReplaceAllString(text, "")
}
```
This function uses the `strings.ReplaceAllString` function with a regular expression to find all vowels in the input string and replace them with an empty string, effectively removing them.

Please note that this function is case-insensitive. If you want it to be case-sensitive, you should remove the `i` flag from the regular expression.