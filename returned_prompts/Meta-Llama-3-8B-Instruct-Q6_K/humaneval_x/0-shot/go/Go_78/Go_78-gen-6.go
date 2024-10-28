You can use a helper function `isPrime` to check if a number is prime, and then count the number of prime hexadecimal digits in the input string. Here is the solution:

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
	for _, c := range num {
		if c >= '0' && c <= '9' {
			digit, _ := strconv.Atoi(string(c))
		} else if c >= 'A' && c <= 'F' {
			digit = int(c - 'A' + 10)
		} else {
			continue
		}
		if isPrime(digit) {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HexKey("AB"))  // 1
	fmt.Println(HexKey("1077E"))  // 2
	fmt.Println(HexKey("ABED1A33"))  // 4
	fmt.Println(HexKey("123456789ABCDEF0"))  // 6
	fmt.Println(HexKey("2020"))  // 2
}
```

This solution iterates over each character in the input string, checks if it's a hexadecimal digit, converts it to a decimal number, and checks if it's prime. If it is, it increments the count. Finally, it returns the count. The `isPrime` function checks if a number is prime by dividing it by all numbers up to its square root. The `HexKey` function uses this helper function to count the prime hexadecimal digits. The `main` function tests the `HexKey` function with different inputs.