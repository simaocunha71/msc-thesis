
    for i := 0; ; i++ {
        pow := math.Pow(float64(n), float64(i))
        if pow == float64(x) {
            return true
        } else if pow > float64(x) {
            return false
        }
    }
}

*/

package main

import (
	"fmt"
	"math"
)

func IsSimplePower(x int, n int) bool {

	for i := 0; ; i++ {
		pow := math.Pow(float64(n), float64(i))
		if pow == float64(x) {
			return true
		} else if pow > float64(x) {
			return false
		}
	}
}

func main() {
	fmt.Println(IsSimplePower(1, 4))  // true
	fmt.Println(IsSimplePower(2, 2))  // true
	fmt.Println(IsSimplePower(8, 2))  // true
	fmt.Println(IsSimplePower(3, 2))  // false
	fmt.Println(IsSimplePower(3, 1))  // false
	fmt.Println(IsSimplePower(5, 3))  // false
}
package main

import (
	"fmt"
	"sort"
)

// 