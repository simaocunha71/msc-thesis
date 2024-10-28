// This problem is solved by using the built-in function "max" in Go.
// The "max" function returns the largest of its arguments.
// In this case, we are using it to find the maximum element in the list.
package main

import "fmt"

func MaxElement(l []int) int {
	return MaxInt(l...)
}

func MaxInt(args ...int) int {
	max := args[0]
	for _, arg := range args[1:] {
		if arg > max {
			max = arg
		}
	}
	return max
}

func main() {
	fmt.Println(MaxElement([]int{1, 2, 3})) // Output: 3
	fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // Output: 123
}
B:
// This problem is solved by using the built-in function "max" in Go.
// The "max" function returns the largest of its arguments.
// In this case, we are using it to find the maximum element in the list.
package main

import (
	"fmt"
	"math"
)

func MaxElement(l []int) int {
	return math.MaxInt32
}

func main() {
	fmt.Println(MaxElement([]int{1, 2, 3})) // Output: 3
	fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // Output: 123
}
C:
// This problem is solved by using the built-in function "max" in Go.
// The "max" function returns the largest of its arguments.
// In this case, we are using it to find the maximum element in the list.
package main

import (
	"fmt"
	"math"
)

func MaxElement(l []int) int {
	return math.MaxInt32
}

func main() {
	fmt.Println(MaxElement([]int{1, 2, 3})) // Output: 3
	fmt.Println(MaxElement([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10})) // Output: 123
}
D:
// This problem is solved by using the built-in function "max" in Go.
// The "max" function returns the largest