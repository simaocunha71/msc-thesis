package main

import (
	"fmt"
)

func Eat(number, need, remaining int) []int {
	eaten := number + need
	left := remaining - need
	if left < 0 {
		left = 0
	}
	return []int{eaten, left}
}

func main() {
	fmt.Println(Eat(5, 6, 10)) // [11, 4]
	fmt.Println(Eat(4, 8, 9)) // [12, 1]
	fmt.Println(Eat(1, 10, 10)) // [11, 0]
	fmt.Println(Eat(2, 11, 5)) // [7, 0]
}