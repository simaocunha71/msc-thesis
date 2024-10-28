    sum := 0.0

B:
    for _, num := range lst {
        sum += math.Pow(math.Ceil(num), 2)
    }

C:
    return int(sum)
}
*/

package main

import (
	"fmt"
	"math"
)

func SumSquares(lst []float64) int {
	sum := 0.0
	for _, num := range lst {
		sum += math.Pow(math.Ceil(num), 2)
	}
	return int(sum)
}

func main() {
	fmt.Println(SumSquares([]float64{1, 2, 3}))         // should print 14
	fmt.Println(SumSquares([]float64{1, 4, 9}))         // should print 98
	fmt.Println(SumSquares([]float64{1, 3, 5, 7}))      // should print 84
	fmt.Println(SumSquares([]float64{1.4, 4.2, 0}))     // should print 29
	fmt.Println(SumSquares([]float64{-2.4, 1, 1}))      // should print 6
}
package main

import (
	"fmt"
	"strings"
)

// Given a string, you need to replace every letter with its position in the alphabet. If anything in the text isn't a letter, leave it as is.
// Examples:
// AlphabetPosition("a") should return "1"
// AlphabetPosition("A") should return "1"
// AlphabetPosition("Test") should return "20 19 23 5"
// AlphabetPosition("Codewars") should return "3 15 4 5 18 23 18 20 13 15"

func AlphabetPosition(text string) string {
	result := []string{}
	for _, ch := range text {
		if 'a' <= ch && ch <= 'z