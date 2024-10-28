
return len(str)

}

*/
package main

import (
	"fmt"
)

func Strlen(str string) int {
	return len(str)
}

func main() {
	fmt.Println(Strlen(""))
	fmt.Println(Strlen("abc"))
}
package main

import (
	"fmt"
	"math"
)

func IsPrime(n int) bool {
	if n <= 1 {
		return false
	}
	if n == 2 {
		return true
	}
	if n%2 == 0 {
		return false
	}
	sqrt := int(math.Sqrt(float64(n)))
	for i := 3; i <= sqrt; i += 2 {
		if n%i == 0 {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(IsPrime(2))
	fmt.Println(IsPrime(1))
	fmt.Println(IsPrime(121))
	fmt.Println(IsPrime(101))
}
package main

import (
	"fmt"
	"math"
)

// 质因数分解
func PrimeFactors(n int) []int {
	var factors []int
	sqrt := int(math.Sqrt(float64(n)))
	for i := 2; i <= sqrt; i++ {
		for n%i == 0 {
			factors = append(factors, i)
			n /= i
		}
	}
	if n > 1 {
		factors = append(factors, n)
	}
	return factors
}

func main() {
	fmt.Println(PrimeFactors(100))
}
package main

import (
	"fmt"
)

func BubbleSort(arr []int) []int {
	n := len(arr)
	for i := 0; i < n; i++ {
		for j := 0; j < n-i-1; j++ {
			if arr[j] >