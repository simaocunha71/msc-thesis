	binary := ""
	for decimal > 0 {
		remainder := decimal % 2
		binary = fmt.Sprintf("%d%s", remainder, binary)
		decimal = decimal / 2
	}
	return fmt.Sprintf("db%sdb", binary)
}

func main() {
	fmt.Println(DecimalToBinary(15))
	fmt.Println(DecimalToBinary(32))
}

// Output:
// db1111db
// db100000db
// Process finished with exit code 0
*/

// Explanation:
// In the DecimalToBinary function, we are converting the given decimal number to binary. We do this by continuously dividing the number by 2 and storing the remainder. The binary representation is created by concatenating these remainders in reverse order.
// The Sprintf function is used to format the binary number string with 'db' at the beginning and end.
// In the main function, we are testing the DecimalToBinary function with decimal numbers 15 and 32. The expected output is "db1111db" and "db100000db" respectively.

package main

import (
	"fmt"
)

func DecimalToBinary(decimal int) string {
	binary := ""
	for decimal > 0 {
		remainder := decimal % 2
		binary = fmt.Sprintf("%d%s", remainder, binary)
		decimal = decimal / 2
	}
	return fmt.Sprintf("db%sdb", binary)
}

func main() {
	fmt.Println(DecimalToBinary(15))
	fmt.Println(DecimalToBinary(32))
}

// Output:
// db1111db
// db100000db
// Process finished with exit code 0

// This code will output the binary representation of the decimal numbers 15 and 32, prefixed and suffixed with "db".
// The binary representation of 15 is 1111 and of 32 is 100000, so the expected output is "db