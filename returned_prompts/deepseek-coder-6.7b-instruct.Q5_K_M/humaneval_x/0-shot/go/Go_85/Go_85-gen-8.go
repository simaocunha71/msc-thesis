
	sum := 0
	for i, v := range lst {
		if i%2 == 1 && v%2 == 0 {
			sum += v
		}
	}
	return sum
}

*/

package main

import (
	"fmt"
)

func Add(lst []int) int {

	sum := 0
	for i, v := range lst {
		if i%2 == 1 && v%2 == 0 {
			sum += v
		}
	}
	return sum
}

func main() {

	lst := []int{4, 2, 6, 7}
	fmt.Println(Add(lst))

}
package main

import (
	"testing"
)

func TestAdd(t *testing.T) {

	tables := []struct {
		x []int
		expected int
	}{
		{[]int{4, 2, 6, 7}, 2},
		{[]int{1, 2, 3, 4, 5, 6}, 4},
		{[]int{10, 20, 30, 40, 50, 60}, 10},
		{[]int{100, 200, 300, 400, 500, 600}, 100},
		{[]int{1000, 2000, 3000, 4000, 5000, 6000}, 1000},
		{[]int{1, 1, 1, 1, 1, 1}, 0},
	}

	for _, table := range tables {
		total := Add(table.x)
		if total != table.expected {
			t.Errorf("Sum of even elements at odd indices of %d was incorrect, got: %d, want: %d.", table.x, total, table.expected)
		}
	}
}

func BenchmarkAdd(b *testing.B) {

	for i :