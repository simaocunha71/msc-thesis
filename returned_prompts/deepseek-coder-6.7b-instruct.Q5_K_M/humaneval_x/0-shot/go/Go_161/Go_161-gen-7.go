
	res := make([]rune, len(s))
	hasLetter := false
	for i, c := range s {
		if unicode.IsLetter(c) {
			hasLetter = true
			if unicode.IsUpper(c) {
				res[i] = unicode.ToLower(c)
			} else {
				res[i] = unicode.ToUpper(c)
			}
		} else {
			res[i] = c
		}
	}
	if !hasLetter {
		for i, j := 0, len(s)-1; i < j; i, j = i+1, j-1 {
			res[i], res[j] = res[j], res[i]
		}
	}
	return string(res)
}

*/

func TestSolve(t *testing.T) {
	tests := []struct {
		input string
		want  string
	}{
		{"1234", "4321"},
		{"ab", "AB"},
		{"#a@C", "#A@c"},
		{"HelloWorld", "hELLOwORLD"},
		{"1234567890", "0987654321"},
		{"aBcDeFgHiZ", "AbCdEfGhIz"},
	}

	for _, test := range tests {
		if got := Solve(test.input); got != test.want {
			t.Errorf("Solve(%q) = %q, want %q", test.input, got, test.want)
		}
	}
}

func BenchmarkSolve(b *testing.B) {
	for i := 0; i < b.N; i++ {
		Solve("HelloWorld")
	}
}
package main

import (
	"fmt"
	"strings"
	"unicode"
)

func Solve(s string) string {
	runes := []rune(s)
	hasLetter := false