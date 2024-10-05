
    sum := 0
    product := 1

    for _, number := range numbers {
        sum += number
        product *= number
    }

    return [2]int{sum, product}
}

func main() {
    fmt.Println(SumProduct([]int{}))  // should print: [0 1]
    fmt.Println(SumProduct([...]int{1, 2, 3, 4}))  // should print: [10 24]
}
*/

package main

import (
	"fmt"
)

func SumProduct(numbers []int) (int, int) {
	sum := 0
	product := 1

	for _, number := range numbers {
		sum += number
		product *= number
	}

	return sum, product
}

func main() {
	fmt.Println(SumProduct([]int{}))         // should print: [0 1]
	fmt.Println(SumProduct([]int{1, 2, 3, 4})) // should print: [10 24]
}

// For a given list of integers, return a tuple consisting of a sum and a product of all the integers in a list.
// Empty sum should be equal to 0 and empty product should be equal to 1.
// √ ✓
// 2
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √ ✓
// √