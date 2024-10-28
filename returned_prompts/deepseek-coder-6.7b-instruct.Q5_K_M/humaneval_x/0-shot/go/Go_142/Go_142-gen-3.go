    sum := 0
    for i, num := range lst {
        switch {
        case i%3 == 0 && i%4 != 0:
            sum += int(math.Pow(float64(num), 2))
        case i%4 == 0:
            sum += int(math.Pow(float64(num), 3))
        default:
            sum += num
        }
    }
    return sum
}

*/

package main

import (
	"fmt"
	"math"
)

func SumSquares(lst []int) int {
	sum := 0
	for i, num := range lst {
		switch {
		case i%3 == 0 && i%4 != 0:
			sum += int(math.Pow(float64(num), 2))
		case i%4 == 0:
			sum += int(math.Pow(float64(num), 3))
		default:
			sum += num
		}
	}
	return sum
}

func main() {
	fmt.Println(SumSquares([]int{1, 2, 3})) // 9
	fmt.Println(SumSquares([]int{}))          // 0
	fmt.Println(SumSquares([]int{-1, -5, 2, -1, -5})) //-126
}
package main

import (
	"fmt"
	"strings"
)

func findLongest(str string) string {
	vowels := []rune{'a', 'e', 'i', 'o', 'u'}
	longest := ""
	curr := ""
	for _, c := range strings.ToLower(str) {
		if containsRune(vowels, c) {
			curr += string(c)
			if len(curr) > len(longest) {
				longest = curr
			}
		} else {
			curr = ""
		}
	}
	if longest == "" {
		return "There are no vowels in the