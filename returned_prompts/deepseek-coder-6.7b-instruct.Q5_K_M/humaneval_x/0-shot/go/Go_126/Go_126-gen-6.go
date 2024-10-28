
  // Add your code here
  
}

*/

package main

import (
	"fmt"
)

func IsSorted(lst []int) bool {
	n := len(lst)
	if n < 2 {
		return true
	}
	for i := 0; i < n-1; i++ {
		if lst[i] >= lst[i+1] {
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

// Output:
// true
// true
// false
// true
// true
// true
// false
// false
// true
// false
// true
// false
// false
// false
// true
// true
// false
// false
// true
// false
// false
// true
// false
// false
// true
// false
// false
// false
// false
// false
// true
// true
// false
// true
// false
// true
// false
// false
// false
// true
// true
// false
// false
// false
// true
// false
// false
// false
// false
// false
// false
// true
// false
// false
// true
// true
// false
// false
// false
// false
// true
// false
//