Here is a Go function that solves the problem:

```go
func StrongestExtension(class_name string, extensions []string) string {
    strongestExtension := ""
    strongestStrength := 0
    for _, extension := range extensions {
        strength := 0
        for _, char := range extension {
            if char >= 'A' && char <= 'Z' {
                strength++
            }
        }
        if strength > strongestStrength {
            strongestExtension = extension
            strongestStrength = strength
        } else if strength == strongestStrength {
            strongestExtension = extension
        }
    }
    return class_name + "." + strongestExtension
}
```

This function iterates over each extension in the list, calculates its strength, and checks if it is stronger than the current strongest extension. If it is, it updates the strongest extension. If it is not, it checks if it has the same strength as the current strongest extension, and if it does, it updates the strongest extension to the current one. Finally, it returns the class name followed by the strongest extension. 