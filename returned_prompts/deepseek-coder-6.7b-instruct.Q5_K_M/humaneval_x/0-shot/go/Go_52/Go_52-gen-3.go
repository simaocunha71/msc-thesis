
// 1. Iterate over the list l.
// 2. For each number in the list, check if it is below the threshold t.
// 3. If any number is not below the threshold, return false.
// 4. If all numbers are below the threshold, return true.

for _, v := range l {

    if v >= t {

        return false

    }

}

return true

}

*/

/*

// Testing the function
package main

import "fmt"

func main() {

    fmt.Println(BelowThreshold([]int{1, 2, 4, 10}, 100)) // Expected true
    fmt.Println(BelowThreshold([]int{1, 20, 4, 10}, 5))  // Expected false

}

*/

package main

import "fmt"

func BelowThreshold(l []int, t int) bool {

	for _, v := range l {
		if v >= t {
			return false
		}
	}

	return true

}

func main() {
	fmt.Println(BelowThreshold([]int{1, 2, 4, 10}, 100)) // Expected true
	fmt.Println(BelowThreshold([]int{1, 20, 4, 10}, 5))  // Expected false
}
package main

import (
	"fmt"
	"strings"
)

/*

