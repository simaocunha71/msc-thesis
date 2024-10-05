	res := make([]int, 0)
	res = append(res, 2)
	res = append(res, 3)

B:
	i := 5
	isPrime := true
C:
	for {
		limit := int(math.Sqrt(float64(i))) + 1
		for j := 2; j < limit; j++ {
			if i%j == 0 {
				isPrime = false
				break
			}
		}
		if isPrime {
			res = append(res, i)
			if len(res) == n {
				return res[n-1]
			}
		}
		i++
		isPrime = true
	}
	return 0
}
*/

package main

import (
	"fmt"
	"math"
)

func PrimeFib(n int) int {
	res := make([]int, 0, n)
	res = append(res, 2)
	res = append(res, 3)

	i := 5
	for len(res) < n {
		limit := int(math.Sqrt(float64(i))) + 1
		for j := 2; j < limit; j++ {
			if i%j == 0 {
				i++
				break
			}
		} else {
			res = append(res, i)
		}
		i++
	}

	return res[n-1]
}

func main() {
	fmt.Println(PrimeFib(1)) // 2
	fmt.Println(PrimeFib(2)) // 3
	fmt.Println(PrimeFib(3)) // 5
	fmt.Println(PrimeFib(4)) // 13
	fmt.Println(PrimeFib(5)) // 89
}
package main

import (
	"fmt"
	"sync"
)

var wg sync.WaitGroup

func printNumbers() {
	for i := 1; i <= 5; i++ {
