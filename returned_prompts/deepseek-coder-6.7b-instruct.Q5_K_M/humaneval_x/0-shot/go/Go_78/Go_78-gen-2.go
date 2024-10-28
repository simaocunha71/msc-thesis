
}

*/

package main

import (
	"fmt"
	"strings"
)

func HexKey(num string) int {
	count := 0
	hexPrimes := []string{"2", "3", "5", "7", "B", "D"}
	for _, char := range num {
		if strings.Contains(strings.Join(hexPrimes[:], ""), string(char)) {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HexKey("AB"))                  // 1
	fmt.Println(HexKey("1077E"))               // 2
	fmt.Println(HexKey("ABED1A33"))            // 4
	fmt.Println(HexKey("123456789ABCDEF0"))    // 6
	fmt.Println(HexKey("2020"))                // 2
}
package main

import (
	"fmt"
	"strings"
)

// HexKey function to count the number of hexadecimal digits that are primes in a given hexadecimal number.
func HexKey(num string) int {
	count := 0
	hexPrimes := []string{"2", "3", "5", "7", "B", "D"}
	for _, char := range num {
		if strings.Contains(strings.Join(hexPrimes[:], ""), string(char)) {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HexKey("AB"))                  // 1
	fmt.Println(HexKey("1077E"))               // 2
	fmt.Println(HexKey("ABED1A33"))            // 4
	fmt.Println(HexKey("123456789ABCDEF0"))    // 6
	fmt.Println(HexKey("2020"))                // 2
}
package main

import (
	"fmt"
)

// Function