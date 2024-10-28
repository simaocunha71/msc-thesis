Here is the solution in Go:

```go
func StrongestExtension(class_name string, extensions []string) string {
    var strongest_extension string
    var max_strength float64
    for _, extension := range extensions {
        strength := float64(len([]rune(extension))) - float64(len([]rune(extension))) - float64(len([]rune(extension)))
        if strength > max_strength {
            max_strength = strength
            strongest_extension = extension
        }
    }
    return class_name + "." + strongest_extension
}
```

This function iterates over each extension in the list. It calculates the strength of the extension as the difference between the number of uppercase and lowercase letters in the extension's name. It keeps track of the strongest extension seen so far and the strength of that extension. When it finds an extension with a strength greater than the current strongest extension, it updates the strongest extension and its strength. Finally, it returns the class name followed by the strongest extension. If there are multiple extensions with the same strength, it will return the one that comes first in the list.