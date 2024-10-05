package main

import "fmt"

var primes = map[byte]int{
	'2': 2,
	'3': 3,
	'5': 5,
	'7': 7,
	'B': 11,
	'D': 13,
}

func HexKey(num string) int {
	count := 0
	for _, c := range num {
		if _, ok := primes[byte(c)]; ok {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HexKey("AB"))        // 1
	fmt.Println(HexKey("1077E"))     // 2
	fmt.Println(HexKey("ABED1A33"))  // 4
	fmt.Println(HexKey("123456789ABCDEF0")) // 6
	fmt.Println(HexKey("2020"))      // 2
}