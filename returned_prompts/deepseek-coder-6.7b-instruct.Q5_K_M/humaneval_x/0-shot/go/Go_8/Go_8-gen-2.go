
    sum := 0
    product := 1
    for _, num := range numbers {
        sum += num
        product *= num
    }
    return [2]int{sum, product}
}

func main() {
    fmt.Println(SumProduct([]int{}))         // should print [0 1]
    fmt.Println(SumProduct([]int{1, 2, 3, 4})) // should print [10 24]
}
*/

package main

import "fmt"

func SumProduct(numbers []int) (int, int) {
	sum := 0
	product := 1
	for _, num := range numbers {
		sum += num
		product *= num
	}
	return sum, product
}

func main() {
	fmt.Println(SumProduct([]int{}))         // should print 0, 1
	fmt.Println(SumProduct([]int{1, 2, 3, 4})) // should print 10, 24
}
package main

import (
	"fmt"
	"sort"
	"strings"
)

/*
