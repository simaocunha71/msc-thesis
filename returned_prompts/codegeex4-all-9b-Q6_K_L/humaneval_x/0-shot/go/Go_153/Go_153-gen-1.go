```go
func StrongestExtension(class_name string, extensions []string) string {
    max := math.Inf(-1)
    var max_ext string
    for _, ext := range extensions {
        cap, sm := 0.0, 0.0
        for _, c := range ext {
            if c >= 'A' && c <= 'Z' {
                cap++
            } else if c >= 'a' && c <= 'z' {
                sm++
            }
        }
        if max < cap-sm {
            max = cap-sm
            max_ext = ext
        }
    }
    return class_name + "." + max_ext
}
```