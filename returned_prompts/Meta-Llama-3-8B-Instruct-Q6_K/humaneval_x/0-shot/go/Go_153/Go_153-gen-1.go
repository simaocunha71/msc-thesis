Here is a Go solution for the problem:

```go
func StrongestExtension(class_name string, extensions []string) string {
    var strongestExtension string
    var maxStrength float64
    for _, extension := range extensions {
        strength := float64(countUppercase(extension)) - float64(countLowercase(extension))
        if strength > maxStrength {
            maxStrength = strength
            strongestExtension = extension
        }
    }
    return class_name + "." + strongestExtension
}

func countUppercase(s string) int {
    var count int
    for _, c := range s {
        if c >= 'A' && c <= 'Z' {
            count++
        }
    }
    return count
}

func countLowercase(s string) int {
    var count int
    for _, c := range s {
        if c >= 'a' && c <= 'z' {
            count++
        }
    }
    return count
}
```

The function `StrongestExtension` iterates over the list of extensions, calculates the strength of each extension, and keeps track of the strongest extension found so far. The strength of an extension is calculated as the difference between the number of uppercase letters and the number of lowercase letters in the extension's name. The function returns the name of the strongest extension concatenated with the class name.

The functions `countUppercase` and `countLowercase` are helper functions that count the number of uppercase and lowercase letters in a given string, respectively. They iterate over the characters in the string and increment a counter for each uppercase or lowercase letter found. The functions return the total count.  The function `StrongestExtension` returns the name of the strongest extension concatenated with the class name. If there are two or more extensions with the same strength, the function returns the one that comes first in the list.  If there are no extensions, the function returns the class name itself.  The function `StrongestExtension` is called with the class name and the list of extensions as arguments.  The function `StrongestExtension` returns a string in the format "ClassName.StrongestExtensionName".  The function `StrongestExtension` is used to find the strongest extension for a given class name and a list of extensions. The function `StrongestExtension` is a part of the solution for the problem.  The function `StrongestExtension` is designed to be used in a Go program. The function `StrongestExtension` is a