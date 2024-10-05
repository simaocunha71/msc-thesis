
    sum := 0

    for _, c := range x {
        if unicode.IsUpper(c) {
            sum += int(c)
        }
    }

    return sum

}

// Note: The ASCII value of 'A' is 65 and 'Z' is 90.
// All uppercase letters in the ASCII table are between these two values.
// Therefore, we can use the 'unicode' package to check if a character is uppercase.
// If it is, we add its ASCII value to our sum.
// We return the sum as the result.


*/
package main

import (
	"fmt"
)

func Digitsum(x string) int {

	sum := 0

	for _, c := range x {
		if c >= 'A' && c <= 'Z' {
			sum += int(c)
		}
	}

	return sum

}

func main() {

	fmt.Println(Digitsum(""))
	fmt.Println(Digitsum("abAB"))
	fmt.Println(Digitsum("abcCd"))
	fmt.Println(Digitsum("helloE"))
	fmt.Println(Digitsum("woArBld"))
	fmt.Println(Digitsum("aAaaaXa"))

}

// Output:
// 0
// 131
// 67
// 69
// 131
// 153

/*

The program works by iterating over each character in the input string. If the character is an uppercase letter (A-Z), it adds the ASCII value of that character to the sum. The result is the sum of the ASCII values of all uppercase letters in the string.

*/
/*

Create a function that takes a string and returns a string with the first character of each word capitalized.

Examples:

    makeTitle("I am a title") ➞ "I Am A Title"
    makeTitle("first letter of every word") ➞ "First Letter Of Every Word"
    makeTitle("ELEMENTS