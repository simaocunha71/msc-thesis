
    var sum int
    for i, v := range lst {
        if i % 2 == 0 && v % 2 != 0 {
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

func Solution(lst []int) int {

	var sum int
	for i, v := range lst {
		if i%2 == 0 && v%2 != 0 {
			sum += v
		}
	}
	return sum
}

func main() {
	fmt.Println(Solution([]int{5, 8, 7, 1}))
	fmt.Println(Solution([]int{3, 3, 3, 3, 3}))
	fmt.Println(Solution([]int{30, 13, 24, 321}))
}

// Expected output:
// 12
// 9
// 0

// This solution works by iterating over the list and checking the index and value of each element.
// If the index is even (i % 2 == 0) and the value is odd (v % 2 != 0), the value is added to the sum.
// Finally, the sum of the odd values at even positions is returned.
package main

import (
	"fmt"
	"math"
)

/*
