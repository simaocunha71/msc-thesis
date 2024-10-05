```go
func StrongestExtension(class_name string, extensions []string) string {
    var strongest = math.Inf(-1)
    var strongest_name = ""
    for _, extension := range extensions {
        cap, sm := 0, 0
        for _, c := range extension {
            if c >= 'A' && c <= 'Z' {
                cap++
            } else if c >= 'a' && c <= 'z' {
                sm++
            }
        }
        strength := float64(cap-sm)
        if strength > strongest {
            strongest = strength
            strongest_name = extension
        }
    }
    return class_name + "." + strongest_name
}
```
