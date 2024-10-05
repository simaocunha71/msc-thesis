Here is the solution to the problem:

```go
import (
    "math"
    "strings"
)

func StrongestExtension(class_name string, extensions []string) string {
    maxStrength := -math.MaxFloat64
    strongestExtension := ""

    for _, extension := range extensions {
        strength := float64(strings.Count(extension, strings.ToUpper(extension))) - float64(strings.Count(extension, strings.ToLower(extension)))
        if strength > maxStrength {
            maxStrength = strength
            strongestExtension = extension
        }
    }

    return class_name + "." + strongestExtension
}
```

Explanation:
The function `StrongestExtension` takes two inputs: `class_name` (a string) and `extensions` (a slice of strings). It iterates over each extension in the slice, calculates its strength using the formula `CAP - SM`, and checks if it's greater than the current maximum strength. If it is, it updates the maximum strength and the strongest extension. Finally, it returns the class name followed by the strongest extension, separated by a dot. The `strings.Count` function is used to count the number of uppercase and lowercase letters in the extension. The `math.MaxFloat64` constant is used as the initial value for the maximum strength to ensure that any calculated strength will be greater than it. The `strings.ToUpper` and `strings.ToLower` functions are used to convert the extension to uppercase and lowercase, respectively, for counting the letters. The `strings.Count` function returns the number of non-space characters in the string that match the given string. If the given string is an empty string, it returns the number of non-space characters in the original string. If the given string is a non-empty string, it returns 1. If the given string is not a string, it returns an error. The function returns the class name followed by the strongest extension, separated by a dot. If there are two or more extensions with the same strength, it chooses the one that comes first in the list. The function does not handle errors and assumes that the inputs are valid. It does not check if the class name is empty or if the extensions slice is empty. It does not check if the extensions slice contains empty strings or if it contains non-string values. It does not check if the extensions slice contains duplicate values. It does not check if the extensions slice contains values that are not strings. It does not check if the extensions slice contains values that are not empty. It does not check if the extensions slice contains values that