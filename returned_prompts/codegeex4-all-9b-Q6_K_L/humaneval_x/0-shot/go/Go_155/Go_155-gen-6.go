package kata

import (
	"strconv"
)

func EvenOddCount(num int) [2]int {
	even := 0
	odd := 0
	str := strconv.Itoa(num)
	for _, r := range str {
		n, _ := strconv.Atoi(string(r))
		if n%2 == 0 {
			even++
		} else {
			odd++
		}
	}
	return [2]int{even, odd}
}