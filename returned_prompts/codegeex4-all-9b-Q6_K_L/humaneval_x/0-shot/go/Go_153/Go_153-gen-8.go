```go
func StrongestExtension(class_name string, extensions []string) string {
    if len(extensions) == 0 {
        return class_name
    }
    var (
        max_strength float64
        max_index    int
    )
    for i, ext := range extensions {
        strength := float64(count_uppercase(ext)) - float64(count_lowercase(ext))
        if strength > max_strength {
            max_strength = strength
            max_index = i
        }
    }
    return fmt.Sprintf("%s.%s", class_name, extensions[max_index])
}

func count_uppercase(s string) (count int) {
    for _, c := range s {
        if c >= 'A' && c <= 'Z' {
            count++
        }
    }
    return
}

func count_lowercase(s string) (count int) {
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            count++
        }
    }
    return
}
```
