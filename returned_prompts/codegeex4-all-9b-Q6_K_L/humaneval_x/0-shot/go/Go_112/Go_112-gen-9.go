```go
func ReverseDelete(s,c string) [2]interface{} {
    var result strings.Builder
    for _, ch := range s {
        if !strings.ContainsRune(c, ch) {
            result.WriteRune(ch)
        }
    }
    resultString := result.String()
    isPalindrome := resultString == reverse(resultString)
    return [2]interface{}{resultString, isPalindrome}
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```