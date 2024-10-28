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
	fmt.Println(HexKey("AB"))       // 1
	fmt.Println(HexKey("1077E"))    // 2
	fmt.Println(HexKey("ABED1A33")) // 4
	fmt.Println(HexKey("123456789ABCDEF0")) // 6
	fmt.Println(HexKey("2020"))     // 2
}
```


Explanation:
The problem is to count the number of hexadecimal digits in a given string that are prime numbers. The function `HexKey` takes a string as input, and it returns the count of prime hexadecimal digits.

Here is the implementation of the function `HexKey` in Go language:

1. First, we define a helper function `isPrime` that checks whether a given integer is prime or not. This function uses a simple trial division method to check for primality.

2. In the `HexKey` function, we iterate over each character in the input string. If the character is a digit (between '0' and '9'), we convert it to an integer using `strconv.Atoi`. If the character is a letter (between 'A' and 'F'), we subtract the ASCII value of 'A' from the character to get the decimal value of the hexadecimal digit. We ignore any other characters.

3. For each digit, we check whether it is prime using the `isPrime` function. If it is prime, we increment the count.

4. Finally, we return the count of prime hexadecimal digits.

In the `main` function, we test the `HexKey` function with different input strings and print the results. The