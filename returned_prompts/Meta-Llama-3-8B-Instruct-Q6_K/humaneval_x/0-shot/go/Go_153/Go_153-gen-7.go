Here is a possible implementation of the `StrongestExtension` function in Go:
```go
package main

import (
    "math"
    "strings"
)

func StrongestExtension(class_name string, extensions []string) string {
    strongestExtension := ""
    strongestStrength := -math.MaxFloat64

    for _, extension := range extensions {
        cap := 0
        sm := 0
        for _, r := range extension {
            if unicode.IsUpper(r) {
                cap++
            } else {
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

func main() {
    class_name := "Slices"
    extensions := []string{"SErviNGSliCes", "Cheese", "StuFfed"}
    result := StrongestExtension(class_name, extensions)
    println(result)  // Output: Slices.SErviNGSliCes
}
```
This implementation uses a loop to iterate over the extensions, and for each extension, it calculates the strength using the formula `CAP - SM` divided by the length of the extension. It keeps track of the strongest extension found so far and returns the class name followed by the strongest extension.

Note that this implementation uses the `unicode.IsUpper` function to check if a rune is an uppercase letter, and the `strings.Range` function to iterate over the runes in the extension. The `math.MaxFloat64` constant is used to initialize the `strongestStrength` variable to a very large value, so that the first extension will always be considered the strongest. Finally, the `println` function is used to print the result to the console.