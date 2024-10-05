
	total := 0

	for i := 0; i < len(lst); i += 2 {
		if lst[i] % 2 != 0 {
			total += lst[i]
		}
	}

	return total
}

*/

package main

import "fmt"

func Solution(lst []int) int {
	total := 0

	for i := 0; i < len(lst); i += 2 {
		if lst[i]%2 != 0 {
			total += lst[i]
		}
	}

	return total
}

func main() {
	fmt.Println(Solution([]int{5, 8, 7, 1}))      // 12
	fmt.Println(Solution([]int{3, 3, 3, 3, 3}))    // 9
	fmt.Println(Solution([]int{30, 13, 24, 321}))  // 0
}
package main

import (
	"fmt"
	"strconv"
	"strings"
)

/*
