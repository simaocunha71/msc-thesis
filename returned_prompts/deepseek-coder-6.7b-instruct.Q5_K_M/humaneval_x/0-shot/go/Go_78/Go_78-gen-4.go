
// Your solution should be written here

}
*/

func HexKey(num string) int {
	primeDigits := map[rune]bool{
		'2': true,
		'3': true,
		'5': true,
		'7': true,
		'B': true,
		'D': true,
	}

	count := 0
	for _, digit := range num {
		if _, ok := primeDigits[digit]; ok {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HexKey("AB"))                  // Should print 1
	fmt.Println(HexKey("1077E"))               // Should print 2
	fmt.Println(HexKey("ABED1A33"))            // Should print 4
	fmt.Println(HexKey("123456789ABCDEF0"))    // Should print 6
	fmt.Println(HexKey("2020"))                // Should print 2
}

// end
package main

import (
	"fmt"
)

// Begin

/*
