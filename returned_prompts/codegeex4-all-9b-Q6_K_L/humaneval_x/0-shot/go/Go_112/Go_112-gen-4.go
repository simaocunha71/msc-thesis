```go
func ReverseDelete(s,c string) [2]interface{} {
    str := strings.Builder{}
    for _, v := range s {
        if !strings.ContainsRune(c, v) {
            str.WriteRune(v)
        }
    }
    if str.String() == reverse(str.String()) {
        return [2]interface{}{str.String(), true}
    }
    return [2]interface{}{str.String(), false}
}

func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```
