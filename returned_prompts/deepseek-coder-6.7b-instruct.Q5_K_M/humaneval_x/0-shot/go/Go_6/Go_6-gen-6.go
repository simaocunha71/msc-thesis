    res := []int{}

    for _, group := range strings.Split(paren_string, " ") {
        max_depth := 0
        current_depth := 0

        for _, char := range group {
            switch char {
            case '(':
                current_depth += 1
                max_depth = int(math.Max(float64(max_depth), float64(current_depth)))
            case ')':
                current_depth -= 1
            }
        }

        res = append(res, max_depth)
    }

    return res
}

*/
package main

import (
	"fmt"
	"strings"
	"math"
)

func ParseNestedParens(paren_string string) []int {
	res := []int{}

	for _, group := range strings.Split(paren_string, " ") {
		max_depth := 0
		current_depth := 0

		for _, char := range group {
			switch char {
			case '(':
				current_depth += 1
				max_depth = int(math.Max(float64(max_depth), float64(current_depth)))
			case ')':
				current_depth -= 1
			}
		}

		res = append(res, max_depth)
	}

	return res
}

func main() {
	res := ParseNestedParens("(()()) ((())) () ((())()())")
	fmt.Println(res) // [2, 3, 1, 3]
}
























































































































