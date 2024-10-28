```go
func ReverseDelete(s,c string) [2]interface{} {
    var t []rune
    for _,i := range s {
        if strings.IndexRune(c,i) == -1 {
            t = append(t,i)
        }
    }
    r := string(t)
    return [2]interface{}{r,r == reverse(r)}
}
func reverse(s string) string {
    runes := []rune(s)
    for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
        runes[i], runes[j] = runes[j], runes[i]
    }
    return string(runes)
}
```