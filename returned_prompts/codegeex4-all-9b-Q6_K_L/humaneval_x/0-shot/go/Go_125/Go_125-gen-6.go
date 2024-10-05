```go
func SplitWords(txt string) interface{} {
    if strings.ContainsAny(txt, " ") {
        return strings.Split(txt, " ")
    }
    if strings.ContainsAny(txt, ",") {
        return strings.Split(txt, ",")
    }
    count := 0
    for _, c := range txt {
        if c >= 'a' && c <= 'z' && (c-'a')%2 == 1 {
            count++
        }
    }
    return count
}
```
