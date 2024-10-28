import (
	"fmt"
)

// You will be given a number in binary format and your task is to convert it to decimal
// format. The function should return an integer.
// 
// There will be an extra couple of characters 'db' at the beginning and at the end of the string.
// The extra characters are there to help with the format.
// 
// Examples:
// BinaryToDecimal("db1111db")   # returns 15
// BinaryToDecimal("db100000db") # returns 32
func BinaryToDecimal(binary string) int {

B:
import (
	"fmt"
)

// You will be given a number in hexadecimal format and your task is to convert it to binary
// format. The function should return a string, with each character representing a binary
// number. Each character in the string will be '0' or '1'.
// 
// There will be an extra couple of characters '0x' at the beginning of the string.
// The extra characters are there to help with the format.
// 
// Examples:
// HexaToBinary("0xF")   # returns "db1111db"
// HexaToBinary("0x10")  # returns "db100000db"
func HexaToBinary(hexa string) string {

C:
import (
	"fmt"
)

// You will be given a number in binary format and your task is to convert it to hexadecimal
// format. The function should return a string, with each character representing a hexadecimal
// number. Each character in the string will be '0' through '9', 'A' through 'F'.
// 
// There will be an extra couple of characters 'db' at the beginning and at the end of the string.
// The extra characters are there to help with the format.
// 
// Examples:
// BinaryToHexa("db1111db")   # returns "0xF"
// BinaryToHexa("db100000db") # returns "0x10"
func BinaryToHexa(binary string) string {