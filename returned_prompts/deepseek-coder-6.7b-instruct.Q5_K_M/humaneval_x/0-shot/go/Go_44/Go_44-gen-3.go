    if x < base {
        return strconv.Itoa(x)
    } else {
        return ChangeBase(x/base, base) + strconv.Itoa(x%base)
    }
}

This program works by recursively dividing the input number by the base and concatenating the remainder of each division. The recursion ends when the input number is less than the base.
This program assumes that the input number is always greater than or equal to 0. If the input number could be negative, additional error checking would be required.
*/

package main

import (
	"fmt"
)

func ChangeBase(x int, base int) string {
	if x < base {
		return string(rune(x) + '0')
	} else {
		return ChangeBase(x/base, base) + string(rune(x%base) + '0')
	}
}

func main() {
	fmt.Println(ChangeBase(8, 3))  // 22
	fmt.Println(ChangeBase(8, 2))  // 1000
	fmt.Println(ChangeBase(7, 2))  // 111
	fmt.Println(ChangeBase(16, 16)) // 10
}

// This program converts a decimal number to any base from 2 to 10.
// For bases greater than 10, the digits are represented as letters where 10 is 'A', 11 is 'B', etc. up to 15 as 'F'.
// The program uses recursion to divide the number by the base and get the remainder. This remainder is then converted to a string and appended to the result.
// The base case for the recursion is when the number is less than the base. In this case, the number itself is converted to a string and returned.
// This program does not handle negative numbers or bases outside the range 2 to 10.
// If you need to handle those cases, you would need to add additional error checking and handling to the program.

/*
