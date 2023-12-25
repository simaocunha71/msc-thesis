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
    if number < 0 || number > 1000 { return "" } else if number >= 500 {
        return StringRepr(RomanNumerals[number-499][number/100]) + StringRepr(RomanNumerals[number%100-1][number%10]);
    } else {
        return StringRepr(RomanNumerals[number-499][number/100]) + StringRepr(RomanNumerals[number%100-1][number%10]);
    }
}