
	sort.Ints(lst)
	for i := 0; i < len(lst)-1; i++ {
		if lst[i] == lst[i+1] {
			return false
		}
	}
	return true

}

*/

package main

import (
	"fmt"
	"sort"
)

func IsSorted(lst []int) bool {

	sort.Ints(lst)
	for i := 0; i < len(lst)-1; i++ {
		if lst[i] == lst[i+1] {
			return false
		}
	}
	return true

}

func main() {
	fmt.Println(IsSorted([]int{5}))
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5}))
	fmt.Println(IsSorted([]int{1, 3, 2, 4, 5}))
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6}))
	fmt.Println(IsSorted([]int{1, 2, 3, 4, 5, 6, 7}))
	fmt.Println(IsSorted([]int{1, 2, 2, 3, 3, 4}))
	fmt.Println(IsSorted([]int{1, 2, 2, 2, 3, 4}))
}
package main

import (
	"fmt"
	"strings"
)

// A word is on the loose and now it has tried every possible combination of letters, but none of them seem to match the right pattern.
// Your task is to write a function that would take a string and a list of words and returns the word that matches the string.

// In case there are multiple correct answers ( multiple matching words ), return the first matching word.

// For example:

// string = "10011101"
// words = ["one", "two", "three", "four", "five", "six", "seven