```go
func RemoveVowels(text string) string {
    // Create a regex pattern that matches any vowel (both lowercase and uppercase)
    pattern := regexp.MustCompile(`[aeiouAEIOU]`)
    // Use the ReplaceAllString function to replace all occurrences of vowels with an empty string
    return pattern.ReplaceAllString(text, "")
}
```

Explanation:
This function uses the `regexp` package to create a regular expression pattern that matches any vowel (both lowercase and uppercase). It then uses the `ReplaceAllString` function to replace all occurrences of vowels in the input `text` with an empty string, effectively removing them. The resulting string is then returned.