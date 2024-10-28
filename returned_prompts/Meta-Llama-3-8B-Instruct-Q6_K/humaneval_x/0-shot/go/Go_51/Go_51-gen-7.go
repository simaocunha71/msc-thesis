Here is the solution:

```go
func RemoveVowels(text string) string {
    // Create a regular expression pattern that matches all vowels (both lowercase and uppercase)
    pattern := regexp.MustCompile(`[aeiouAEIOU]`)

    // Use the ReplaceAllString function to replace all vowels with an empty string
    return pattern.ReplaceAllString(text, "")
}
```


This solution uses the `regexp` package in Go to create a regular expression pattern that matches all vowels (both lowercase and uppercase). It then uses the `ReplaceAllString` function to replace all occurrences of vowels in the input string with an empty string, effectively removing them. The resulting string is then returned.