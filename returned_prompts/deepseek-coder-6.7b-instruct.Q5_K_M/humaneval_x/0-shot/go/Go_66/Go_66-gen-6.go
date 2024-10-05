
  var sum int = 0
  for _, c := range x {
    if unicode.IsUpper(c) {
      sum += int(c)
    }
  }
  return sum
}

*/

package main

import (
	"fmt"
)

func Digitsum(x string) int {
	var sum int = 0
	for _, c := range x {
		if 'A' <= c && c <= 'Z' {
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

// Explanation:
// In this solution, we iterate over each character in the string. If the character is an uppercase English alphabet letter
// (checked by 'A' <= c && c <= 'Z'), we add its ASCII value to the sum.
// Finally, we return the sum.
// Note: The built-in function unicode.IsUpper() can also be used to check if a character is an uppercase letter.
// However, the ASCII value comparison is more efficient.
package main

import "fmt"

func main() {
	for i := 1; i <= 100; i++ {
		if i%15 == 0 {
			fmt.Println("FizzBuzz")
		} else if i%3 == 0 {
			fmt.Println("Fizz")
		} else if i%5 == 0 {
			fmt.Println("Buzz")
		} else {
			fmt.Println(i)
		}
	}
}

// Explanation:
// This program prints numbers from 1 to 100. For multiples of three, it prints "Fizz" instead of the number and for the multiples of five, it prints "Bu