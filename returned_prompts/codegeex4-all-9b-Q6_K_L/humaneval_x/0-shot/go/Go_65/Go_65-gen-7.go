package main

import (
	"fmt"
	"strconv"
	"strings"
)

func CircularShift(x int, shift int) string {
	str := strconv.Itoa(x)
	l := len(str)
	if shift > l {
		return reverse(str)
	}
	return str[shift:] + str[:shift]
}

func reverse(s string) string {
	r := []rune(s)
	for i, j := 0, len(r)-1; i < j; i, j = i+1, j-1 {
		r[i], r[j] = r[j], r[i]
	}
	return string(r)
}

func main() {
	fmt.Println(CircularShift(12, 1))
	fmt.Println(CircularShift(12, 2))
}