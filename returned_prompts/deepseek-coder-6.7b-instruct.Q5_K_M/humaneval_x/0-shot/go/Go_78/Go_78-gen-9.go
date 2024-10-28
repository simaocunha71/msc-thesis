
}
*/

package main

import "fmt"

func HexKey(num string) int {
	prime_hex := map[rune]bool{
		'2': true,
		'3': true,
		'5': true,
		'7': true,
		'B': true,
		'D': true,
	}

	count := 0
	for _, hex := range num {
		if prime_hex[hex] {
			count++
		}
	}

	return count
}

func main() {
	fmt.Println(HexKey("AB"))
	fmt.Println(HexKey("1077E"))
	fmt.Println(HexKey("ABED1A33"))
	fmt.Println(HexKey("123456789ABCDEF0"))
	fmt.Println(HexKey("2020"))
}

// Output:
// 1
// 2
// 4
// 6
// 2
//
// Process finished with exit code 0

// This function works by first initializing a map to store the prime hexadecimal digits.
// Then, it iterates through the given string 'num' character by character.
// If the character is in the map, it increments the count.
// Finally, it returns the count.
// This count is the number of prime hexadecimal digits in the string.
