```go
func SplitWords(txt string) interface{} {
    if strings.Contains(txt, " ") {
        return strings.Split(txt, " ")
    } else if strings.Contains(txt, ",") {
        return strings.Split(txt, ",")
    }
    n := 0
    for _, c := range txt {
        if c >= 'a' && c <= 'z' && (c-'a')%2 == 1 {
            n++
        }
    }
    return n
}
```
