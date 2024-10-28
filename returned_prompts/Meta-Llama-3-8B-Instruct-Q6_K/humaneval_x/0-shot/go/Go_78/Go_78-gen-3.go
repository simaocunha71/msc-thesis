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
	count := 0
	for _, c := range num {
		if c >= '2' && c <= '9' {
			digit, _ := strconv.ParseInt(string(c), 10, 10)
			if isPrime(int(digit)) {
				count++
			}
		} else if c >= 'A' && c <= 'F' {
			digit, _ := strconv.ParseInt(string(c), 16, 10)
			if isPrime(int(digit)) {
				count++
			}
		}
	}
	return count
}

func main() {
	fmt.Println(HexKey("AB"))  // Output: 1
	fmt.Println(HexKey("1077E")) // Output: 2
	fmt.Println(HexKey("ABED1A33")) // Output: 4
	fmt.Println(HexKey("123456789ABCDEF0")) // Output: 6
	fmt.Println(HexKey("2020")) // Output: 2
}
```


Explanation:

The provided Go code defines a function called `HexKey` that takes a hexadecimal number as a string and returns the count of hexadecimal digits that are prime numbers. The function iterates over each character in the input string and checks if the character represents a hexadecimal digit (either a digit from 0 to 9 or a letter from A to F). For each digit, it converts the digit to an integer using the `strconv.ParseInt` function and checks if the integer is a prime number using the `isPrime` function. If the integer is a prime number, it increments the count. Finally, the function returns the count of prime hexadecimal digits.

The `isPrime` function checks if a given integer is a prime number by iterating from 2 to the square root of the number and checking if the number is divisible by any of the numbers in that range. If the number is not divisible by any of the numbers in that range, it is considered a prime number.

In the `main` function, the code tests the `HexKey` function with different input strings and prints the output. The output is