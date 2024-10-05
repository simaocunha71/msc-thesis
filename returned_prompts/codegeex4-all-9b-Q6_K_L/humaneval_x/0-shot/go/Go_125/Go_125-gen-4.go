```go
func SplitWords(txt string) interface{} {
    if strings.Count(txt, " ") == 0 {
        if strings.Count(txt, ",") == 0 {
            odd := 0
            for _, c := range txt {
                if c >= 'a' && c <= 'z' {
                    if (c-'a')%2 == 1 {
                        odd++
                    }
                }
            }
            return odd
        } else {
            return strings.Split(txt, ",")
        }
    } else {
        return strings.Split(txt, " ")
    }
}
```
