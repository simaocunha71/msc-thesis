
	// your code here
	var r string
	hasLetter := false
	for _, c := range s {
		if unicode.IsLetter(c) {
			hasLetter = true
			if unicode.IsLower(c) {
				r += strings.ToUpper(string(c))
			} else {
				r += strings.ToLower(string(c))
			}
		} else {
			r += string(c)
		}
	}
	if !hasLetter {
		r = reverse(r)
	}
	return r
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}


*/

package main

import (
	"fmt"
	"unicode"
)

func Solve(s string) string {
	var r string
	hasLetter := false
	for _, c := range s {
		if unicode.IsLetter(c) {
			hasLetter = true
			if unicode.IsLower(c) {
				r += strings.ToUpper(string(c))
			} else {
				r += strings.ToLower(string(c))
			}
		} else {
			r += string(c)
		}
	}
	if !hasLetter {
		r = reverse(r)
	}
	return r
}

func reverse(s string) string {
	runes := []rune(s)
	for i, j := 0, len(runes)-1; i < j; i, j = i+1, j-1 {
		runes[i], runes[j] = runes[j], runes[i]
	}
	return string(runes)
}

func main() {
	fmt.Println(Solve("1234"))
	fmt.Println(