
1. Initialize an empty list.
2. Iterate over the input list.
3. For each element, if it is not in the new list, add it.
4. Return the new list.

*/

package main

import (
	"fmt"
)

func RemoveDuplicates(numbers []int) []int {
	newNumbers := []int{}
	numbersMap := make(map[int]bool)

	for _, num := range numbers {
		if _, exists := numbersMap[num]; !exists {
			numbersMap[num] = true
			newNumbers = append(newNumbers, num)
		}
	}

	return newNumbers
}

func main() {
	numbers := []int{1, 2, 3, 2, 4}
	result := RemoveDuplicates(numbers)
	fmt.Println(result) // Prints [1, 2, 3, 4]
}
package main

import (
	"fmt"
	"strings"
)

// 