
// Initialize a variable to hold the sum
    sum := 0

// Iterate over the string
    for _, char := range x {

// Check if the character is uppercase
        if char >= 'A' && char <= 'Z' {

// Add its ASCII code to the sum
            sum += int(char)
        }
    }

// Return the sum
    return sum
}

*/
package main

import (
	"fmt"
)

func Digitsum(x string) int {
	sum := 0
	for _, char := range x {
		if char >= 'A' && char <= 'Z' {
			sum += int(char)
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
	fmt.Println(Digitsum(""))         // 0
}

/*

This function works by iterating over the string and checking if each character is uppercase. If it is, the ASCII code of that character is added to the sum.

The function returns the sum of the ASCII codes of all uppercase characters in the string.

*/
package main

import (
	"fmt"
)

func main() {

	var a int = 5
	var b int = 10

	// addition
	sum := a + b
	fmt.Printf("Sum: %d\n", sum)

	// subtraction
	diff := b - a
	fmt.Printf("Difference: %d\n", diff)

	// multiplication
	product := a * b
	fmt.Printf("Product: %d\n", product)

	// division
	quotient := b / a
	fmt.Printf("Quotient