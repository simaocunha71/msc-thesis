import (
    "strings"
)

// For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
// >>> FlipCase('Hello')
// 'hELLO'
func FlipCase(str string) string {
    var result strings.Builder
    for _, r := range str {
        if unicode.IsLower(r) {
            result.WriteRune(unicode.ToUpper(r))
        } else if unicode.IsUpper(r) {
            result.WriteRune(unicode.ToLower(r))
        } else {
            result.WriteRune(r)
        }
    }
    return result.String()
}

B:
import (
    "strings"
    "unicode"
)

// For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
// >>> FlipCase('Hello')
// 'hELLO'
func FlipCase(str string) string {
    var result strings.Builder
    for _, r := range str {
        if unicode.IsLower(r) {
            result.WriteRune(unicode.ToUpper(r))
        } else if unicode.IsUpper(r) {
            result.WriteRune(unicode.ToLower(r))
        } else {
            result.WriteRune(r)
        }
    }
    return result.String()
}

C:
import (
    "strings"
)

// For a given string, flip lowercase characters to uppercase and uppercase to lowercase.
// >>> FlipCase('Hello')
// 'hELLO'
func FlipCase(str string) string {
    var result strings.Builder
    for i, r := range str {
        if i%2 == 0 {
            result.WriteRune(unicode.ToLower(r))
        } else {
            result.WriteRune(unicode.ToUpper(r))
        }
    }
    return result.String()
}

D:
import (
    "strings"
    "unicode"
)

// For a given string, flip lowercase characters