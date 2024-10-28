package main

import (
	"fmt"
	"strconv"
)

func CircularShift(x int, shift int) string {
	str := strconv.Itoa(x)
	if shift > len(str) {
		return reverse(str)
	}
	return str[shift:] + str[:shift]
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	fmt.Println(CircularShift(12, 1)) // "21"
	fmt.Println(CircularShift(12, 2)) // "12"
}