```go
func RemoveVowels(text string) string {
    re := regexp.MustCompile("[aeiouAEIOU]")
    return re.ReplaceAllString(text, "")
}
```