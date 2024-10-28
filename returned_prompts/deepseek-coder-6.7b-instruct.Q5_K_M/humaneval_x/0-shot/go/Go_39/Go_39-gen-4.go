	a := 1
B:
	b := 1
C:
	c := 0
D:
	i := 2
E:
	j := 0
F:
	primeNumbers := []int{a, b}

	for {
		c = a + b
		a = b
		b = c

		for {
			if c%primeNumbers[j] == 0 {
				break B
			}
			j++
		}

		primeNumbers = append(primeNumbers, c)
		i++
		if i == n {
			break D
		}
		j = 0
	}
	return c
}

func main() {
	fmt.Println(PrimeFib(1))
	fmt.Println(PrimeFib(2))
	fmt.Println(PrimeFib(3))
	fmt.Println(PrimeFib(4))
	fmt.Println(PrimeFib(5))
}
*/

// Solution:

import (
	"fmt"
	"math"
)

func PrimeFib(n int) int {
	a := 1
	b := 1
	c := 0
	primeNumbers := []int{a, b}
	i := 2
	j := 0

	for i < n {
		c = a + b
		a = b
		b = c

		for {
			if c%primeNumbers[j] == 0 {
				break
			}
			j++
		}

		primeNumbers = append(primeNumbers, c)
		i++
		j = 0
	}
	return c
}

func main() {
	fmt.Println(PrimeFib(1))
	fmt.Println(PrimeFib(2))
	fmt.Println(PrimeFib(3))
	fmt.Println(PrimeFib(4))
	fmt.Println(PrimeFib(5))
}

// Output:
// 2
// 3
// 5
// 13
