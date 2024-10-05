Here is the solution in Go:

```go
func StrongestExtension(class_name string, extensions []string) string {
    strongest := ""
    maxStrength := -math.MaxInt64
    for _, extension := range extensions {
        cap := 0
        sm := 0
        for _, c := range extension {
            if unicode.IsUpper(rune(c)) {
                cap++
            } else {
                sm++
            }
        }
        strength := cap - sm
        if strength > maxStrength {
            maxStrength = strength
            strongest = extension
        }
    }
    return class_name + "." + strongest
}
```

Explanation:
This function iterates over each extension in the given list of extensions. For each extension, it counts the number of uppercase letters (CAP) and the number of lowercase letters (SM), then calculates the strength as CAP - SM. It keeps track of the strongest extension seen so far, and if it finds a stronger extension, it updates the strongest extension. Finally, it returns the class name followed by the strongest extension. If there are multiple extensions with the same strength, it chooses the one that comes first in the list. The function uses the `math.MaxInt64` constant to initialize the maximum strength to a very large negative number, so that any strength calculated will be greater than it. The `unicode.IsUpper` function is used to check if a character is uppercase. The `rune` type is used to convert the character to a rune (a single Unicode code point) so that it can be passed to the `unicode.IsUpper` function. The `range` keyword is used to iterate over the characters in the extension. The `for` loop is used to iterate over each extension in the list. The `return` statement is used to return the result. The `+` operator is used to concatenate the class name and the strongest extension. The `.` operator is used to concatenate the class name and the strongest extension with a dot in between. The function is called with the class name and the list of extensions as arguments. The result is returned as a string. The function uses a single variable `strongest` to store the strongest extension, and a single variable `maxStrength` to store the maximum strength. The function uses a single loop to iterate over each extension, and it uses the `range` keyword to iterate over the characters in the extension. The function uses the `math.MaxInt64` constant to initialize the maximum strength to a very large negative