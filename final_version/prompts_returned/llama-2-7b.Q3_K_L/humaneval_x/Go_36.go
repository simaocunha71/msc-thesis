import (
	"strconv"
	"strings"
)

// Return the number of times the digit 7 appears in integers less than n which are divisible by 11 or 13.
// >>> FizzBuzz(50)
// 0
// >>> FizzBuzz(78)
// 2
// >>> FizzBuzz(79)
// 3
func FizzBuzz(n int) int {
	return fizzbuzz(n, 11, 13, "FB")
}

func fizzbuzz(n int, divisor1, divisor2, suffixes []string) int {
	i := 0
	for i < n && i%divisor1 == 0 && i%divisor2 == 0 {
		str := ""
		for j := range suffixes {
			if (n % divisor1 >= divisor2 || n%divisor2 == 0) && str != "FB" && i < n {
				str += suffixes[j]
			} else if !(i < n && n%divisor1 >= divisor2) {
				str = ""
			}
			if j == 0 || str != "" {
				fmt.Printf("%d ", i)
			}
		}
		i++
	}
	return i
}
