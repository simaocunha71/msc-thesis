
// put your code here
return false
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

	isIncreasing := true
	isDecreasing := true

	for i := 0; i < n-1; i++ {
		if lst[i] > lst[i+1] {
			isIncreasing = false
		}
		if lst[i] < lst[i+1] {
			isDecreasing = false
		}
		if !isIncreasing && !isDecreasing {
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
package main

import (
	"fmt"
	"os"
	"strings"
)

func main() {
	name := os.Args[1]
	msg := fmt.Sprintf("Hello, %s", strings.Title(name))
	fmt.Println(msg)
}

// to run the program, use:
// go run main.go [name]
// e.g., go run main.go john
// Output: Hello, John
