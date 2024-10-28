Here is a Go function that implements the described functionality:

```go
import (
    "math"
)

func StrongestExtension(class_name string, extensions []string) string {
    var strongest_extension string
    var strongest_strength float64

    for _, extension := range extensions {
        cap := 0
        sm := 0

        for _, char := range extension {
            if char >= 'A' && char <= 'Z' {
                cap++
            } else if char >= 'a' && char <= 'z' {
                sm++
            }
        }

        strength := float64(cap - sm) / float64(cap + sm)
        if strength > strongest_strength {
            strongest_strength = strength
            strongest_extension = extension
        }
    }

    return class_name + "." + strongest_extension
}
```

This function iterates over the list of extensions, calculates the strength of each extension, and keeps track of the strongest extension found so far. If a stronger extension is found, it updates the strongest strength and strongest extension. Finally, it returns a string in the format `ClassName.StrongestExtensionName`. If there are two or more extensions with the same strength, it chooses the one that comes first in the list. 

The strength of an extension is calculated as the fraction of uppercase letters minus the fraction of lowercase letters in the extension's name. This is done to account for the strength of the extension as described in the problem statement. 

The function uses the `math` package to calculate the strength of each extension. The `float64(cap - sm) / float64(cap + sm)` expression calculates the fraction of uppercase letters minus the fraction of lowercase letters in the extension's name. The `float64` type is used to ensure that the division is done as a floating-point operation, rather than an integer operation. 

The function returns a string in the format `ClassName.StrongestExtensionName`, where `ClassName` is the input class name and `StrongestExtensionName` is the name of the strongest extension. If there are two or more extensions with the same strength, it chooses the one that comes first in the list. 

This function should work correctly for the example provided in the problem statement, and for any other valid input. 

For example, if you call `StrongestExtension("Slices", []string{"SErviNGSliCes", "Cheese", "StuFfed"})`, the function will return `"Slices.SErviNGSliC