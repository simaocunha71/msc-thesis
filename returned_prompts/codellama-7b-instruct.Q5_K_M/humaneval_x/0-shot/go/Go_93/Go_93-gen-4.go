import (
    "bytes"
)

// Write a function that takes a string and returns its rune values
// as a slice.
//
// Examples:
// >>> StringToRunes("abc")
// [97, 98, 99]
// >>> StringToRunes("こんにちは")
// [227, 129, 130, 227, 128, 173, 227, 128, 168, 227, 128, 131]
func StringToRunes(s string) []rune {

