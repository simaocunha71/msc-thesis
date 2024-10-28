	i := 0
	sum := 0
	
	for i < n {
		if i % 11 == 0 || i % 13 == 0 {
			str := strconv.Itoa(i)
			count := strings.Count(str, "7")
			sum += count
		}
		i++
	}
	
	return sum
}
*/

import (
	"strconv"
	"strings"
)

// FizzBuzz returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
func FizzBuzz(n int) int {
	sum := 0
	for i := 0; i < n; i++ {
		if i%11 == 0 || i%13 == 0 {
			str := strconv.Itoa(i)
			count := strings.Count(str, "7")
			sum += count
		}
	}
	return sum
}

// FizzBuzzOptimized returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
// This version is optimized by breaking out of the inner loop once we find a number that isn't divisible by 11 or 13.
func FizzBuzzOptimized(n int) int {
	sum := 0
	for i := 0; i < n; i++ {
		if i%11 != 0 && i%13 != 0 {
			continue
		}
		str := strconv.Itoa(i)
		count := strings.Count(str, "7")
		sum += count
	}
	return sum
}

// FizzBuzzOptimized2 returns the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
// This version is optimized by checking for divisibility by 11 and 13 separately.
func FizzBuzzOptimized2(n int) int {
	sum := 0
	for i := 0; i < n; i += 11 {