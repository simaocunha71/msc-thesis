
	sum := 0
	for _, v := range x {
		if v >= 'A' && v <= 'Z' {
			sum += int(v)
		}
	}
	return sum
}

func main() {

	fmt.Println(Digitsum("abAB")) // 131
	fmt.Println(Digitsum("abcCd")) // 67
	fmt.Println(Digitsum("helloE")) // 69
	fmt.Println(Digitsum("woArBld")) // 131
	fmt.Println(Digitsum("aAaaaXa")) // 153
}

*/

// Solution:
// The function works by iterating through each character in the string. If the character is an uppercase letter (ASCII values from 65 to 90), it adds its ASCII value to a sum variable. Finally, it returns the sum.

package main

import (
	"fmt"
)

func Digitsum(x string) int {
	sum := 0
	for _, v := range x {
		if v >= 'A' && v <= 'Z' {
			sum += int(v)
		}
	}
	return sum
}

func main() {
	fmt.Println(Digitsum("abAB"))     // 131
	fmt.Println(Digitsum("abcCd"))    // 67
	fmt.Println(Digitsum("helloE"))   // 69
	fmt.Println(Digitsum("woArBld"))  // 131
	fmt.Println(Digitsum("aAaaaXa"))  // 153
}

// This program will output the sum of the ASCII values of all uppercase characters in the input string.
// For example, for the input "abAB", the program will output 131 because the uppercase letters 'A' and 'B' have ASCII values of 65 and 66 respectively, and their sum is 131.
// For other inputs, the program will follow the same logic.
// The function does not consider lower