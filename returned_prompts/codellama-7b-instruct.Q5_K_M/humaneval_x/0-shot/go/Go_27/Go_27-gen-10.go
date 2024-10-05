import (
    "strings"
)

// For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
// >>> FlipCase('Hello')
// 'hELLO'
func FlipCase(str string) string {
    var newString strings.Builder
    for _, char := range str {
        if char >= 'a' && char <= 'z' {
            newString.WriteRune(char - 32)
        } else if char >= 'A' && char <= 'Z' {
            newString.WriteRune(char + 32)
        } else {
            newString.WriteRune(char)
        }
    }
    return newString.String()
}
