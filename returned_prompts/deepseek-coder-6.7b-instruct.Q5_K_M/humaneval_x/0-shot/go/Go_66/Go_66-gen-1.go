
	sum := 0
	for _, c := range x {
		if unicode.IsUpper(c) {
			sum += int(c)
		}
	}
	return sum
}

func main()  {

	testCases := []struct {
		input string
		want int
	}{
		{"", 0},
		{"abAB", 131},
		{"abcCd", 67},
		{"helloE", 69},
		{"woArBld", 131},
		{"aAaaaXa", 153},
	}

	for _, tc := range testCases {
		got := Digitsum(tc.input)
		if got != tc.want {
			fmt.Printf("Digitsum(%v) = %v, want %v\n", tc.input, got, tc.want)
		}
	}
}

*/

package main

import (
	"fmt"
	"unicode"
)

func Digitsum(s string) int {
	sum := 0
	for _, c := range s {
		if unicode.IsUpper(c) {
			sum += int(c)
		}
	}
	return sum
}

func main() {
	fmt.Println(Digitsum("abAB"))      // 131
	fmt.Println(Digitsum("abcCd"))     // 67
	fmt.Println(Digitsum("helloE"))    // 69
	fmt.Println(Digitsum("woArBld"))   // 131
	fmt.Println(Digitsum("aAaaaXa"))   // 153
	fmt.Println(Digitsum(""))          // 0
}

































































