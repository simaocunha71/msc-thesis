```go
package main

import (
	"fmt"
	"strconv"
)

func isPrime(n int) bool {
	if n <= 1 {
		return false
	}
	for i := 2; i*i <= n; i++ {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func HexKey(num string) int {
	var count int
	for _, ch := range num {
		if ch >= 'A' && ch <= 'F' {
			digit, _ := strconv.ParseInt(string(ch), 16, 10)
			if isPrime(int(digit)) {
				count++
			}
		} else if ch >= '2' && ch <= '9' {
			digit, _ := strconv.ParseInt(string(ch), 10, 10)
			if isPrime(int(digit)) {
				count++
			}
		}
	}
	return count
}

func main() {
	fmt.Println(HexKey("AB")) // 1
	fmt.Println(HexKey("1077E")) // 2
	fmt.Println(HexKey("ABED1A33")) // 4
	fmt.Println(HexKey("123456789ABCDEF0")) // 6
	fmt.Println(HexKey("2020")) // 2
}
```


In this solution, I created a helper function `isPrime` to check if a number is prime. The `HexKey` function iterates over each character in the input string. If the character is a hexadecimal digit (A-F), it converts it to a decimal number and checks if it is prime. If the character is a decimal digit (2-9), it converts it to a decimal number and checks if it is prime. If the digit is prime, it increments a counter. Finally, the function returns the count of prime digits. In the `main` function, I tested the `HexKey` function with different input strings.