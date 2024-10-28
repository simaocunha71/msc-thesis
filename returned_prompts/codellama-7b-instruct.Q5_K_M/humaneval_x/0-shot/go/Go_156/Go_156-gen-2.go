import (
    "strings"
)

// Given a positive integer, obtain its roman numeral equivalent as a string,
// and return it in lowercase.
// Restrictions: 1 <= num <= 1000
// 
// Examples:
// >>> IntToMiniRoman(19) == 'xix'
// >>> IntToMiniRoman(152) == 'clii'
// >>> IntToMiniRoman(426) == 'cdxxvi'
func IntToMiniRoman(number int) string {
    if number <= 0 {
        return ""
    }
    var result strings.Builder
    for number > 0 {
        switch {
        case number >= 1000:
            result.WriteString("m")
            number -= 1000
        case number >= 900:
            result.WriteString("cm")
            number -= 900
        case number >= 500:
            result.WriteString("d")
            number -= 500
        case number >= 400:
            result.WriteString("cd")
            number -= 400
        case number >= 100:
            result.WriteString("c")
            number -= 100
        case number >= 90:
            result.WriteString("xc")
            number -= 90
        case number >= 50:
            result.WriteString("l")
            number -= 50
        case number >= 40:
            result.WriteString("xl")
            number -= 40
        case number >= 10:
            result.WriteString("x")
            number -= 10
        case number >= 9:
            result.WriteString("ix")
            number -= 9
        case number >= 5:
            result.WriteString("v")
            number -= 5
        case number >= 4:
            result.WriteString("iv")
            number -= 4
        case number == 1:
            result.WriteString("i")
            number -= 1
        }
    }
    return result.String()
}
