package main

import (
	"fmt"
)

func MatchParens(lst []string) string {
	var result []string

	for _, v := range lst {
		if v == "(" || v == ")" {
			result = append(result, v)
		}
	}

	if len(result)%2 == 0 {
		return "Yes"
	} else {
		return "No"
	}
}

func main() {
	fmt.Println(MatchParens([]string{"()", "()"}))
	fmt.Println(MatchParens([]string{"(", ")"}))
}