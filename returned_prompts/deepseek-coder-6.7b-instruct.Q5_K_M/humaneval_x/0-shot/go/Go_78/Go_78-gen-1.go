
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
	fmt.Println(HexKey("AB"))                         // 1
	fmt.Println(HexKey("1077E"))                      // 2
	fmt.Println(HexKey("ABED1A33"))                   // 4
	fmt.Println(HexKey("123456789ABCDEF0"))           // 6
	fmt.Println(HexKey("2020"))                       // 2
	fmt.Println(HexKey("A44C1739F55FB0F3"))           // 4
	fmt.Println(HexKey("161718191A1B1C1D1E1F"))       // 6
	fmt.Println(HexKey("A3B4C5D6E7F8A9BACDED1AB1EA")) // 6
}
package main

import (
	"fmt"
	"math"
)

// 