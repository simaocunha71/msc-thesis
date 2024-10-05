	binary := ""

B:
	for decimal > 0 {
		remainder := decimal % 2
		decimal = decimal / 2
		binary = fmt.Sprintf("%d%s", remainder, binary)
	}

C:
	return "db" + binary + "db"
}

func main() {
	fmt.Println(DecimalToBinary(15))  // returns "db1111db"
	fmt.Println(DecimalToBinary(32))  // returns "db100000db"
}

Output:
db1111db
db100000db

*/

package main

import (
	"fmt"
)

func DecimalToBinary(decimal int) string {

	binary := ""

	for decimal > 0 {
		remainder := decimal % 2
		decimal = decimal / 2
		binary = fmt.Sprintf("%d%s", remainder, binary)
	}

	return "db" + binary + "db"
}

func main() {
	fmt.Println(DecimalToBinary(15))  // returns "db1111db"
	fmt.Println(DecimalToBinary(32))  // returns "db100000db"
}

// Output:
// db1111db
// db100000db

// Solution Explanation:
// This program works by continuously dividing the decimal number by 2 and storing the remainder.
// It then appends the remainder to the binary string. This process is repeated until the decimal number is 0.
// The binary string is then prefixed and suffixed with "db" to meet the problem's requirements.

// The time complexity of this solution is O(log(n)) because we're repeatedly dividing the number by 2.
// The space complexity is also O(log(n)) because we're storing the binary digits in a string.
// Here, n is the input decimal number.

// This solution is correct and efficient because it correctly converts the decimal number to binary format.
// It uses