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

    roman := make([]byte, 0, 16)
    for number > 0 {
        switch {
        case number >= 1000:
            roman = append(roman, 'm')
            number -= 1000
        case number >= 900:
            roman = append(roman, 'm', 'cm')
            number -= 900
        case number >= 500:
            roman = append(roman, 'd', 'c')
            number -= 500
        case number >= 400:
            roman = append(roman, 'cm')
            number -= 400
        case number >= 100:
            roman = append(roman, 'c')
            number -= 100
        case number >= 90:
            roman = append(roman, 'xc')
            number -= 90
        case number >= 50:
            roman = append(roman, 'l', 'x')
            number -= 50
        case number >= 40:
            roman = append(roman, 'xl')
            number -= 40
        case number >= 10:
            roman = append(roman, 'x')
            number -= 10
        case number >= 9:
            roman = append(roman, 'ix')
            number -= 9
        case number >= 5:
            roman = append(roman, 'v', 'i')
            number -= 5
        case number >= 4:
            roman = append(roman, 'iv')
            number -=