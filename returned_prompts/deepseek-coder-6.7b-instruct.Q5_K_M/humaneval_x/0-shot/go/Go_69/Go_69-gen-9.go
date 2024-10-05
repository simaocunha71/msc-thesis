
    sort.Ints(lst)

    max := lst[len(lst)-1]

    frequency := make([]int, max+1)

    for _, num := range lst {
        frequency[num]++
    }

    for i := max; i > 0; i-- {
        if frequency[i] >= i {
            return i
        }
    }

    return -1
}

*/

package main

import (
	"fmt"
	"sort"
)

func Search(lst []int) int {

	sort.Ints(lst)

	max := lst[len(lst)-1]

	frequency := make([]int, max+1)

	for _, num := range lst {
		frequency[num]++
	}

	for i := max; i > 0; i-- {
		if frequency[i] >= i {
			return i
		}
	}

	return -1
}

func main() {
	fmt.Println(Search([]int{4, 1, 2, 2, 3, 1}))
	fmt.Println(Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4}))
	fmt.Println(Search([]int{5, 5, 4, 4, 4}))
}

// Output:
// 2
// 3
// -1
package main

import (
	"fmt"
	"testing"

	"github.com/stretchr/testify/assert"
)

type testStruct struct {
	input    []int
	expected int
}

func TestSearch(t *testing.T) {
	tests := []testStruct{
		{[]int{4, 1, 2, 2, 3, 1}, 2},
		{[]int{1, 2, 2, 3, 3, 3, 4, 4, 4}, 3},
		{[]int{5, 5,