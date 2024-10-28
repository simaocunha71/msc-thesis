```go
func SplitWords(txt string) interface{} {
    if strings.ContainsAny(txt, " ") {
        return strings.Split(txt, " ")
    } else if strings.ContainsAny(txt, ",") {
        return strings.Split(txt, ",")
    } else {
        var res int
        for _, c := range txt {
            if c >= 'a' && c <= 'z' {
                if (c - 'a') % 2 == 1 {
                    res++
                }
            }
        }
        return res
    }
}
```
