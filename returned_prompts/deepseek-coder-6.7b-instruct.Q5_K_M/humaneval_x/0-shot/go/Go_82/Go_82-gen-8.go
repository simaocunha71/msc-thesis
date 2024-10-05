
	length := len(s)
	if length < 2 {
		return false
	}
	for i := 2; i*i <= length; i++ {
		if length%i == 0 {
			return false
		}
	}
	return true

}

*/

package main

import (
	"fmt"
)

func PrimeLength(s string) bool {

	length := len(s)
	if length < 2 {
		return false
	}
	for i := 2; i*i <= length; i++ {
		if length%i == 0 {
			return false
		}
	}
	return true

}

func main() {

	fmt.Println(PrimeLength("Hello")) //== true
	fmt.Println(PrimeLength("abcdcba")) //== true
	fmt.Println(PrimeLength("kittens")) //== true
	fmt.Println(PrimeLength("orange")) //== false
}

























































































































































































































































































