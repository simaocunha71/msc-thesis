
// Write your code here

}

*/

func Eat(number, need, remaining int) []int {
	if remaining >= need {
		number += need
		remaining -= need
		need = 0
	} else if remaining < need {
		number += remaining
		need -= remaining
		remaining = 0
	}
	return []int{number, remaining}
}

func main() {
	fmt.Println(Eat(5, 6, 10))  //[11, 4]
	fmt.Println(Eat(4, 8, 9))  //[12, 1]
	fmt.Println(Eat(1, 10, 10)) //[11, 0]
	fmt.Println(Eat(2, 11, 5))  //[7, 0]
}
package main

import (
	"fmt"
	"strings"
)

// Given a string, return a string where for every char in the original, there are two chars.

// doubleChar("The") → "TThhee"
// doubleChar("AAbb") → "AAAAbbbb"
// doubleChar("Hi-There") → "HHii--TThheerree"

func doubleChar(str string) string {
	var result []string
	for _, v := range str {
		result = append(result, strings.Repeat(string(v), 2))
	}
	return strings.Join(result, "")
}

func main() {
	fmt.Println(doubleChar("The"))
	fmt.Println(doubleChar("AAbb"))
	fmt.Println(doubleChar("Hi-There"))
}
package main

import (
	"fmt"
	"strconv"
	"strings"
)

// Given a number, return a string with dash'-'marks before and after each odd integer, but do not begin or end with a dash mark.

// dashatize(274) -> "2-7-4"
// dashatize(5311) -> "53