
// Write your code here

}

*/

package main

import "fmt"

func Eat(number, need, remaining int) []int {
	if need <= remaining {
		return []int{number + need, remaining - need}
	} else {
		return []int{number + remaining, 0}
	}
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
	"math"
)

// Given a string, return the string with its words in reverse order.

func ReverseWords(str string) string {
	words := make([]string, 0)
	word := ""
	for _, c := range str {
		if c == ' ' {
			words = append(words, word)
			word = ""
		} else {
			word += string(c)
		}
	}
	words = append(words, word)

	result := ""
	for i := len(words) - 1; i >= 0; i-- {
		result += words[i]
		if i != 0 {
			result += " "
		}
	}
	return result
}

// Given a string, return the string with its words in reverse order.
// This function uses a simple stack to solve the problem.

func ReverseWordsStack(str string) string {
	stack := make([]string, 0)
	word := ""
	for _, c := range str {
		if c == ' ' {
			stack = append(stack, word)
			word = ""
		} else {
			word += string(c)
		}
	}
	stack