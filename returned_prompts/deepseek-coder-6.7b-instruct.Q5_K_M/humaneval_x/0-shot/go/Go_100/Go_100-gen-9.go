
	stones := make([]int, n)
	stones[0] = n
	for i := 1; i < n; i++ {
		if stones[i-1]%2 == 0 {
			stones[i] = stones[i-1] + 2
		} else {
			stones[i] = stones[i-1] + 2
		}
	}
	return stones

}

*/

package main

import (
	"fmt"
)

func MakeAPile(n int) []int {
	stones := make([]int, n)
	stones[0] = n
	for i := 1; i < n; i++ {
		if stones[i-1]%2 == 0 {
			stones[i] = stones[i-1] + 2
		} else {
			stones[i] = stones[i-1] + 2
		}
	}
	return stones
}

func main() {
	fmt.Println(MakeAPile(3))
}

// Output:
// [3 5 7]
// Explanation:
// The first level has 3 stones.
// The second level has 5 stones.
// The third level has 7 stones.

/*

Test Cases:

1) MakeAPile(3) 
This should return a list [3, 5, 7] because the first level has 3 stones, the second level has 5 stones, and the third level has 7 stones.

2) MakeAPile(5)
This should return a list [5, 7, 9, 11, 13] because the first level has 5 stones, the second level has 7 stones, and so on up to the fifth level.

3) MakeAPile(10)
This should return a list [10, 12, 14, 16, 18, 20, 22, 24, 26, 28] because each level has an odd number of stones, starting with 10 and increasing by 2 each time.

*/
package main

import