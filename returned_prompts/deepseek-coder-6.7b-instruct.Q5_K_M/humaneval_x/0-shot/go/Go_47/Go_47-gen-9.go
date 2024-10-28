	sort.Ints(l)

B:
	n := len(l)
	if n % 2 == 0 {
		return float64(l[n/2-1] + l[n/2]) / 2.0
	} else {
		return float64(l[n/2])
	}
}

*/

package main

import (
	"fmt"
	"sort"
)

func Median(l []int) float64 {
	sort.Ints(l)
	n := len(l)
	if n%2 == 0 {
		return float64(l[n/2-1] + l[n/2]) / 2.0
	} else {
		return float64(l[n/2])
	}
}

func main() {
	fmt.Println(Median([]int{3, 1, 2, 4, 5}))
	fmt.Println(Median([]int{-10, 4, 6, 1000, 10, 20}))
}
package main

import (
	"fmt"
	"testing"
)

func TestMedian(t *testing.T) {
	var tests = []struct {
		input []int
		want  float64
	}{
		{[]int{3, 1, 2, 4, 5}, 3},
		{[]int{-10, 4, 6, 1000, 10, 20}, 15},
		{[]int{1, 2, 3, 4, 5, 6}, 3.5},
		{[]int{6, 8, 12, 15, 19, 25}, 12},
	}

	for _, test := range tests {
		testname := fmt.Sprintf("%v", test.input)
		t.Run(testname, func(t *testing.T) {
			ans := Median(test.input)
			if ans != test.want {
				t.Errorf("got %