package main

import (
	"fmt"
	"strings"
	"unicode"
)

func Solve(s string) string {
	rev := false
	for _, c := range s {
		if unicode.IsLetter(c) {
			rev = !rev
		}
	}
	if rev {
		s = reverse(s)
	}
	for i, c := range s {
		if unicode.IsLetter(c) {
			if unicode.IsUpper(c) {
				s = strings.Replace(s, string(c), strings.ToLower(string(c)), 1)
			} else {
				s = strings.Replace(s, string(c), strings.ToUpper(string(c)), 1)
			}
		}
	}
	return s
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	fmt.Println(Solve("1234")) // 4321
	fmt.Println(Solve("ab"))   // AB
	fmt.Println(Solve("#a@C")) // #A@c
}