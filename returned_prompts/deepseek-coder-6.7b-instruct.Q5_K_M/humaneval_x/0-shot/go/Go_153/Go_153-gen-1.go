    var max_strength float64 = math.MinInt64
    var strongest_extension string
    for _, extension := range extensions {
        cap_count := 0
        sm_count := 0
        for _, char := range extension {
            if unicode.IsUpper(char) {
                cap_count++
            }
            if unicode.IsLower(char) {
                sm_count++
            }
        }
        strength := float64(cap_count) - float64(sm_count)
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }
    return fmt.Sprintf("%s.%s", class_name, strongest_extension)
}
```

This code loops through each extension in the list and calculates the strength of the extension. The strength is calculated by subtracting the number of lowercase letters from the number of uppercase letters in the extension's name. If the calculated strength is greater than the current maximum strength, the extension is updated as the strongest extension. Finally, the function returns a string in the required format.

If you are interested in the strength of the extension, you can use the function:

```go
func Strength(extension string) float64 {
    cap_count := 0
    sm_count := 0
    for _, char := range extension {
        if unicode.IsUpper(char) {
            cap_count++
        }
        if unicode.IsLower(char) {
            sm_count++
        }
    }
    return float64(cap_count) - float64(sm_count)
}
```

This function takes an extension name as input and returns its strength. It does this by counting the number of uppercase and lowercase letters in the extension name and subtracting the number of lowercase letters from the number of uppercase letters.

I hope this helps. Let me know if you have any other questions.

```go
func StrongestExtension(class_name string, extensions []string) string {
    var max_strength float64 = math.MinInt64
    var strongest_extension string
    for _, extension :