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

    // We are going to use a string builder to build the roman numeral string
    // from the integer.
    var roman string

    // We are going to use a buffer to hold the current digit that we are
    // going to convert to a roman numeral.
    var buffer bytes.Buffer

    // We are going to use a loop to iterate over the digits of the integer.
    for i := 1; i <= number; i++ {

        // We are going to get the remainder of the current digit when
        // divided by 10. We are going to use this to determine which
        // roman numeral to add to the string.
        remainder := i % 10

        // We are going to get the current digit from the integer.
        digit := i / 10

        // We are going to get the next digit from the integer.
        nextDigit := (i + 1) / 10

        // We are going to get the previous digit from the integer.
        previousDigit := (i - 1) / 10

        // We are going to check if the current digit is equal to 1. If
        // it is, we are going to add the corresponding roman numeral to
        // the string.
        if digit == 1 {
            roman += romanNumeralForOne
        }

        // We are going to check if the current digit is equal to 4. If
        // it is, we are going to add the corresponding roman numeral to
        // the string.
        if digit == 4 {
            roman += romanNumeralForFour
        }

        //