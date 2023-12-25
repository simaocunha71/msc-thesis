import (
	"fmt"
)

// You will be given a number in decimal form and your task is to convert it to
// binary format. The function should return a string, with each character representing a binary
// number. Each character in the string will be '0' or '1'.
// 
// There will be an extra couple of characters 'db' at the beginning and at the end of the string.
// The extra characters are there to help with the format.
// 
// Examples:
// DecimalToBinary(15)   # returns "db1111db"
// DecimalToBinary(32)   # returns "db100000db"
func DecimalToBinary(decimal int) string {
	res := make([]byte, 0, decimal+1)

	for k, v := range res {
		if decimal == 0 {
			fmt.Printf("The binary value is: %s\n", hex.EncodeToString(v))
		} else if decimal&1 != 0 || (decimal-1)&256 != 0 || (decimal+1)%8 == 4 {
			fmt.Printf("The binary value is: %s\n", hex.EncodeToString(v))
		} else if decimal&2 == 0 && decimal/2 <= 4 {
			res[k] = byte(decimal/2)
		}
		if decimal%8 != 0 || (decimal-1)/8 <= 4 {
			res[k+1] = byte((decimal - 1) / 8 + 1)
		}
		decimal -= res[k]*256 + res[k+1]*8 + decimal % 8;
	}
	return string(res[0 : len(res)-1])
}
