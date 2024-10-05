```go
package main

import (
    "regexp"
)

// RemoveVowels is a function that takes string and returns string without vowels.
func RemoveVowels(text string) string {
    re := regexp.MustCompile("[aeiouAEIOU]")
    return re.ReplaceAllString(text, "")
}
```
