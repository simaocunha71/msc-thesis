```go
func StrongestExtension(class_name string, extensions []string) string {
    max := math.Inf(-1)
    res := ""
    for _, s := range extensions {
        cap, sm := 0, 0
        for _, c := range s {
            if c >= 'A' && c <= 'Z' {
                cap++
            } else if c >= 'a' && c <= 'z' {
                sm++
            }
        }
        if float64(cap-sm) > max {
            max = float64(cap-sm)
            res = s
        }
    }
    return class_name + "." + res
}
```
