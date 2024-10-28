```go
func StrongestExtension(class_name string, extensions []string) string {
    best_extension := ""
    max_strength := math.MinInt64
    for _, ext := range extensions {
        cap := 0
        sm := 0
        for _, ch := range ext {
            if ch >= 'A' && ch <= 'Z' {
                cap++
            } else if ch >= 'a' && ch <= 'z' {
                sm++
            }
        }
        strength := cap - sm
        if strength > max_strength {
            max_strength = strength
            best_extension = ext
        }
    }
    return class_name + "." + best_extension
}
```
