```go
func ReverseDelete(s,c string) [2]interface{} {
    for i:=0;i<len(c);i++{
        s = strings.Replace(s,string(c[i]),"",-1)
    }
    if s == Reverse(s) {
        return [2]interface{}{s, true}
    } else {
        return [2]interface{}{s, false}
    }
}

func Reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```
