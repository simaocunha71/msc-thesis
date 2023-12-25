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
	str := strings.Repeat(" ", n+1)
	for i := 2; i < strconv.Itoa(len(str))-4; i++ {
		if ((i&7) == 0 && (i%13) == 0) || (i&7) == 7 || (i%13) == 5 {
			return i + str[2]
		} else if (i & 7) == 7 {
			str += "fizz"
		} else if (i % 13) == 5 {
			str += "buzz"
		} else if (i%11) == 0 && (i&7) == 0 {
			continue
		}
		str += strconv.Itoa(i) + "\n"
	}
	return str[len(str)-2:]
}
