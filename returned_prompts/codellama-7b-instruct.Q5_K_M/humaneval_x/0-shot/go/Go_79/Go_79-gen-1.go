import (
	"fmt"
)

// You will be given a number in binary format and your task is to convert it to
// decimal format. The function should return an integer, with each character representing a binary
// number. Each character in the string will be '0' or '1'.
// 
// There will be an extra couple of characters 'db' at the beginning and at the end of the string.
// The extra characters are there to help with the format.
// 
// Examples:
// BinaryToDecimal("db1111db")   # returns 15
// BinaryToDecimal("db100000db")   # returns 32
func BinaryToDecimal(binary string) int {

