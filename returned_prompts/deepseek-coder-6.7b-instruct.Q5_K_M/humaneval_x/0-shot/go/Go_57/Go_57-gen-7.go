
	increasing := true
	decreasing := true

	for i := 0; i < len(l)-1; i++ {
		if l[i] > l[i+1] {
			increasing = false
		}
		if l[i] < l[i+1] {
			decreasing = false
		}
	}

	if increasing {
		return true
	} else if decreasing {
		return true
	} else {
		return false
	}
}

*/

package main

import (
	"fmt"
)

// Return true is list elements are Monotonically increasing or decreasing.
func Monotonic(l []int) bool {

	increasing := true
	decreasing := true

	for i := 0; i < len(l)-1; i++ {
		if l[i] > l[i+1] {
			increasing = false
		}
		if l[i] < l[i+1] {
			decreasing = false
		}
	}

	if increasing {
		return true
	} else if decreasing {
		return true
	} else {
		return false
	}
}

func main() {
	fmt.Println(Monotonic([]int{1, 2, 4, 20}))
	fmt.Println(Monotonic([]int{1, 20, 4, 10}))
	fmt.Println(Monotonic([]int{4, 1, 0, -10}))
}
package main

import (
	"testing"
)

func TestMonotonic(t *testing.T) {
	for _, tc := range []struct {
		name string
		l    []int
		want bool
	}{
		{"monotonic increasing", []int{1, 2, 3, 4, 5}, true},
		{"monotonic decreasing", []int{5, 4, 3, 2, 1}, true},
		{"not monotonic", []int{5, 4, 3, 2, 1,