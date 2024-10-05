```go
func StrongestExtension(class_name string, extensions []string) string {
    var (
        max Strength = Strength(-math.MaxInt)
        ans string
    )
    for _, ext := range extensions {
        strength := Strength(len([]rune(strings.ToUpper(ext))) - len([]rune(ext)))
        if strength > max {
            max = strength
            ans = ext
        }
    }
    return class_name + "." + ans
}
```