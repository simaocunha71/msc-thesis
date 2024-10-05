
// Write your solution here

}

*/

package main

import (
	"fmt"
	"math"
)

func IsMultiplyPrime(a int) bool {
	primeFactors := primeFactors(a)
	return len(primeFactors)%2 == 1
}

func primeFactors(n int) []int {
	var factors []int
	for i := 2; i <= int(math.Sqrt(float64(n))); i++ {
		if n%i == 0 {
			n /= i
			factors = append(factors, i)
			i--
		}
	}
	if n > 1 {
		factors = append(factors, n)
	}
	return factors
}

func main() {
	fmt.Println(IsMultiplyPrime(30)) // true
	fmt.Println(IsMultiplyPrime(42)) // true
	fmt.Println(IsMultiplyPrime(100)) // false
	fmt.Println(IsMultiplyPrime(180)) // true
	fmt.Println(IsMultiplyPrime(360)) // false
}
package main

import (
	"fmt"
	"strings"
)

func getMaxOccuringChar(str string) (string, int) {
	var maxChar string
	var maxCount int
	charCounts := make(map[string]int)

	for _, char := range strings.ToLower(str) {
		charCounts[string(char)]++
	}

	for char, count := range charCounts {
		if count > maxCount {
			maxChar = char
			maxCount = count
		}
	}

	return maxChar, maxCount
}

func main() {
	char, count := getMaxOccuringChar("Hello World")
	fmt.Printf("The most frequently occurring character is '%s' with a count of %d\n", char, count)
}
package main

import (
	"fmt"
	"strings"
)

func isAnagram(str