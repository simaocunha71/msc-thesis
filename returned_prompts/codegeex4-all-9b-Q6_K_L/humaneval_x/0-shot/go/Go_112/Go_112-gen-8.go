```go
func ReverseDelete(s,c string) [2]interface{} {
    result := strings.ReplaceAll(s, c, "")
    if result == reverse(result) {
        return [2]interface{}{result, true}
    }
    return [2]interface{}{result, false}
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```
