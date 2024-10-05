
}

*/

package main

import (
	"fmt"
	"strings"
)

func HexKey(num string) int {
	primes := []string{"2", "3", "5", "7", "B", "D"}
	count := 0
	for _, digit := range num {
		if strings.Contains(strings.Join(primes, ""), string(digit)) {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HexKey("AB"))              // 1
	fmt.Println(HexKey("1077E"))           // 2
	fmt.Println(HexKey("ABED1A33"))        // 4
	fmt.Println(HexKey("123456789ABCDEF0")) // 6
	fmt.Println(HexKey("2020"))            // 2
}
package main

import (
	"fmt"
	"strings"
)

func HexKey(num string) int {
	hexDigits := []string{"2", "3", "5", "7", "B", "D"}
	count := 0
	for _, digit := range num {
		if strings.Contains(strings.Join(hexDigits, ""), string(digit)) {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HexKey("AB"))              // 1
	fmt.Println(HexKey("1077E"))           // 2
	fmt.Println(HexKey("ABED1A33"))        // 4
	fmt.Println(HexKey("123456789ABCDEF0")) // 6
	fmt.Println(HexKey("2020"))            // 2
}

/*
