```go
func StrongestExtension(class_name string, extensions []string) string {
    max := math.MinInt
    maxStr := ""
    for _, ext := range extensions {
        upper := 0
        lower := 0
        for _, c := range ext {
            if c >= 'A' && c <= 'Z' {
                upper++
            } else if c >= 'a' && c <= 'z' {
                lower++
            }
        }
        if upper-lower > max {
            max = upper - lower
            maxStr = ext
        }
    }
    return class_name + "." + maxStr
}
```
