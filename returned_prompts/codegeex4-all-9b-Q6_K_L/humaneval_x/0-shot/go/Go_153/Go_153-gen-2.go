```go
func StrongestExtension(class_name string, extensions []string) string {
    max_strength := math.Inf(-1)
    strongest_extension := ""
    for _, ext := range extensions {
        strength := 0
        for _, ch := range ext {
            if ch >= 'A' && ch <= 'Z' {
                strength++
            } else if ch >= 'a' && ch <= 'z' {
                strength--
            }
        }
        if strength > max_strength {
            max_strength = strength
            strongest_extension = ext
        }
    }
    return class_name + "." + strongest_extension
}
```
