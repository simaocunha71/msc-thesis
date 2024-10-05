
}
*/

package main

import (
	"fmt"
	"strings"
)

func HexKey(num string) int {
	primeHex := []string{"2", "3", "5", "7", "B", "D"}
	count := 0
	for _, v := range num {
		if strings.Contains(strings.Join(primeHex[:], ""), string(v)) {
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
/*
