
result := make([]int, 0, len(numbers)*2-1)

	for i, num := range numbers {
		result = append(result, num)
		if i != len(numbers)-1 {
			result = append(result, delimeter)
		}
	}
	
	return result
}

*/

package main

import (
	"fmt"
)

// Intersperse inserts delimeter between every two consecutive elements of input list numbers
func Intersperse(numbers []int, delimeter int) []int {
	result := make([]int, 0, len(numbers)*2-1)

	for i, num := range numbers {
		result = append(result, num)
		if i != len(numbers)-1 {
			result = append(result, delimeter)
		}
	}

	return result
}

func main() {
	fmt.Println(Intersperse([]int{}, 4))       // []
	fmt.Println(Intersperse([]int{1, 2, 3}, 4)) // [1, 4, 2, 4, 3]
}
package main

import (
	"fmt"
	"strings"
)

// Reverse reverses the input string
func Reverse(s string) string {
	var result strings.Builder
	runes := []rune(s)
	for i := len(runes) - 1; i >= 0; i-- {
		result.WriteRune(runes[i])
	}
	return result.String()
}

func main() {
	fmt.Println(Reverse("Hello, World!")) // "olleH, !dlroW"
}
/*
