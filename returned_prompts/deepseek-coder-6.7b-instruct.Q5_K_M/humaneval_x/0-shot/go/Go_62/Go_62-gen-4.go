
    result := make([]int, len(xs) - 1)
    for i := 1; i < len(xs); i++ {
        result[i-1] = xs[i] * i
    }
    return result
}

*/

package main

import (
	"fmt"
)

func Derivative(xs []int) []int {

	result := make([]int, len(xs)-1)
	for i := 1; i < len(xs); i++ {
		result[i-1] = xs[i] * i
	}
	return result
}

func main() {
	fmt.Println(Derivative([]int{3, 1, 2, 4, 5})) // [1, 4, 12, 20]
	fmt.Println(Derivative([]int{1, 2, 3}))         // [2, 6]
}
package main

import (
	"fmt"
)

func SplitByValue(k int, elements []int) [][]int {
	less := make([]int, 0)
	equal := make([]int, 0)
	greater := make([]int, 0)

	for _, el := range elements {
		switch {
		case el < k:
			less = append(less, el)
		case el == k:
			equal = append(equal, el)
		case el > k:
			greater = append(greater, el)
		}
	}

	return [][]int{less, equal, greater}
}

func main() {
	fmt.Println(SplitByValue(5, []int{1, 3, 5, 7, 9, 5, 5, 7, 10, 1, 3}))
	// [[1 3 1] [5 5 5] [7 9 10 3]]
}
package main

import (
	"fmt"
	"sort"
)

func IsAnagram(test, original string) bool