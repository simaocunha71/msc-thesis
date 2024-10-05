```go
func StrongestExtension(class_name string, extensions []string) string {
    max := math.Inf(-1)
    best := ""
    for _, ext := range extensions {
        cap := 0
        small := 0
        for _, c := range ext {
            if c >= 'A' && c <= 'Z' {
                cap++
            } else if c >= 'a' && c <= 'z' {
                small++
            }
        }
        strength := float64(cap - small)
        if strength > max {
            max = strength
            best = ext
        }
    }
    return class_name + "." + best
}
```
