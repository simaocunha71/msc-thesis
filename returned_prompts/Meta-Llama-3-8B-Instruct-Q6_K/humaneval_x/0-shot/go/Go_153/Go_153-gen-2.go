Here is the solution:

```go
func StrongestExtension(class_name string, extensions []string) string {
    var strongest_extension string
    var strongest_strength float64
    for _, extension := range extensions {
        var cap int
        var sm int
        for _, char := range extension {
            if char >= 'A' && char <= 'Z' {
                cap++
            } else if char >= 'a' && char <= 'z' {
                sm++
            }
        }
        strength := float64(cap - sm)
        if strength > strongest_strength {
            strongest_extension = extension
            strongest_strength = strength
        }
    }
    return class_name + "." + strongest_extension
}
```

This function iterates over each extension in the list and calculates its strength by counting the number of uppercase letters (CAP) and the number of lowercase letters (SM). It then checks if the current extension's strength is greater than the strongest strength found so far. If it is, it updates the strongest extension and the strongest strength. Finally, it returns the class name followed by the strongest extension. If there are multiple extensions with the same strongest strength, it will choose the first one in the list.

The function `StrongestExtension` takes two parameters: `class_name` (a string representing the name of a class) and `extensions` (a slice of strings representing the extensions). It returns a string in the format `ClassName.StrongestExtensionName`.

The time complexity of this function is O(n), where n is the number of extensions, because it iterates over each extension once. The space complexity is O(1), because it uses a constant amount of space to store the strongest extension and the strongest strength. 