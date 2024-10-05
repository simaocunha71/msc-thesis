```go
func SplitWords(txt string) interface{} {
    words := strings.Fields(txt)
    if len(words) > 0 {
        return words
    }
    words = strings.Split(txt, ",")
    if len(words) > 0 {
        return words
    }
    count := 0
    for _, r := range txt {
        if unicode.IsLower(r) && (r-'a')%2 == 1 {
            count++
        }
    }
    return count
}
```
