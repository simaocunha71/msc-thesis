
// Base case:
// If a equals to b return a
if a == b {
return a
}

// If a is greater than b, replace a with the difference between a and b
if a > b {
return GreatestCommonDivisor(a-b, b)
}

// If b is greater than a, replace b with the difference between b and a
if b > a {
return GreatestCommonDivisor(a, b-a)
}

}
*/

import (
	"fmt"
)

func GreatestCommonDivisor(a int, b int) int {
	for b != 0 {
		a, b = b, a%b
	}
	return a
}

func main() {
	fmt.Println(GreatestCommonDivisor(3, 5))
	fmt.Println(GreatestCommonDivisor(25, 15))
}
package main

import "fmt"

func isPalindrome(x int) bool {
	if x < 0 {
		return false
	}
	reverse := 0
	original := x
	for x != 0 {
		reverse = reverse*10 + x%10
		x = x / 10
	}
	return original == reverse
}

func main() {
	fmt.Println(isPalindrome(121)) // true
	fmt.Println(isPalindrome(-121)) // false
	fmt.Println(isPalindrome(10)) // false
}
package main

import (
	"fmt"
	"math"
)

func reverse(x int) int {
	var res int
	for x != 0 {
		pop := x % 10
		x = x / 10
		if res > math.MaxInt32/10 || (res == math.MaxInt32/10 && pop > 7) {
			return 0
		}
		if res < math.MinInt32/10 || (res == math.MinInt32/10 && pop < -8) {
			return 0
		}
		