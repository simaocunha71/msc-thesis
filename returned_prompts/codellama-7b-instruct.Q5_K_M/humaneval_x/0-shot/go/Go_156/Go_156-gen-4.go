import (
    "fmt"
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

    // Create a mapping of numbers to roman numerals
    // 1 => "i"
    // 4 => "iv"
    // 5 => "v"
    // 9 => "ix"
    // 10 => "x"
    // 40 => "xl"
    // 50 => "l"
    // 90 => "xc"
    // 100 => "c"
    // 400 => "cd"
    // 500 => "d"
    // 900 => "cm"
    // 1000 => "m"
    //
    // Create a slice to hold the roman numerals
    //
    // Iterate from 1 to number, adding the corresponding roman numerals to the slice
    //
    // Join the slice into a single string
    //
    // Return the string
}

