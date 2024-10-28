    bin := ""
    sum := 0

    for N > 0 {
        digit := N % 10
        sum += digit
        N /= 10
    }

    for sum > 0 {
        bin = strconv.Itoa(sum%2) + bin
        sum /= 2
    }

    return bin
}

func main() {
    fmt.Println(Solve(1000))
    fmt.Println(Solve(150))
    fmt.Println(Solve(147))
}

*/
package main

import (
	"fmt"
	"strconv"
)

func Solve(N int) string {
	bin := ""
	sum := 0

	for N > 0 {
		digit := N % 10
		sum += digit
		N /= 10
	}

	for sum > 0 {
		bin = strconv.Itoa(sum%2) + bin
		sum /= 2
	}

	return bin
}

func main() {
	fmt.Println(Solve(1000))
	fmt.Println(Solve(150))
	fmt.Println(Solve(147))
}
package main

import (
	"fmt"
)

func Solve(N int) int {
	count := 0
	for i := 1; i <= N; i++ {
		if isEvenDigits(i) && hasAdjacentDigits(i) {
			count++
		}
	}
	return count
}

func isEvenDigits(n int) bool {
	digits := getDigits(n)
	return len(digits)%2 == 0
}

func getDigits(n int) []int {
	digits := []int{}
	for n > 0 {
		digit := n % 10
		digits = append(digits, digit)
		n /= 10
	}
	return digits
}

func hasAdjacentDigits(n int) bool {