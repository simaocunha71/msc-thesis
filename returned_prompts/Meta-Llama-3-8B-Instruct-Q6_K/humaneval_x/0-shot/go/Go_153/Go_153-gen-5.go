Here is a possible implementation of the `StrongestExtension` function in Go:
```go
func StrongestExtension(class_name string, extensions []string) string {
    strongestExtension := ""
    strongestStrength := 0

    for _, extension := range extensions {
        cap := 0
        sm := 0

        for _, c := range extension {
            if unicode.IsUpper(c) {
                cap++
            } else if unicode.IsLower(c) {
                sm++
            }
        }

        strength := float64(cap - sm) / float64(len(extension))

        if strength > strongestStrength {
            strongestExtension = extension
            strongestStrength = strength
        }
    }

    return class_name + "." + strongestExtension
}
```
This function iterates over the list of extensions, calculates the strength of each extension using the formula `CAP - SM` divided by the length of the extension, and keeps track of the strongest extension and its strength. Finally, it returns the class name followed by the strongest extension name. If there are multiple extensions with the same strength, it returns the one that comes first in the list.

Note that this implementation uses the `unicode` package to check if a character is uppercase or lowercase, and the `float64` type to perform the division. The `range` keyword is used to iterate over the characters in the extension name. The `math` package is not actually needed in this implementation, as the division is performed using the `/` operator, which performs integer division when both operands are integers, and floating-point division when one or both operands are floating-point numbers. However, it is included in the import statement to avoid errors if the division is modified to use a different type.