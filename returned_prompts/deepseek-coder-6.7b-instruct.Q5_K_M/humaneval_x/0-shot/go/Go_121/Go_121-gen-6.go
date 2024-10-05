
// Start by defining the sum variable to hold the sum of the odd elements.
sum := 0

// Iterate over the list using a for loop, using the index i to check if the element is at an even position.
for i := range lst {

// Check if the element is odd by checking if the modulus of the element divided by 2 is not equal to 0.
    if lst[i] % 2 != 0 {

// If the element is odd and at an even position (i is even), add it to the sum.
        sum += lst[i]
    }
}

// Return the sum.
return sum
}

*/

package main

import "fmt"

func Solution(lst []int) int {
	sum := 0
	for i := range lst {
		if lst[i]%2 != 0 && i%2 == 0 {
			sum += lst[i]
		}
	}
	return sum
}

func main() {
	fmt.Println(Solution([]int{5, 8, 7, 1}))        // should be 12
	fmt.Println(Solution([]int{3, 3, 3, 3, 3}))     // should be 9
	fmt.Println(Solution([]int{30, 13, 24, 321}))    // should be 0
	fmt.Println(Solution([]int{2, 2, 2, 2, 2, 2, 2})) // should be 2
}
package main

import (
	"fmt"
	"strings"
)

func Solution(s string) string {
	words := strings.Fields(s)
	for i, word := range words {
		if i%2 == 0 {
			words[i] = strings.ToUpper(word)
		} else {
			words[i] = strings.ToLower(word)
		}
	}
	return strings.Join(words, " ")
}

func main() {
	fmt.Println(Solution("hello world