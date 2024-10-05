    sort.Ints(lst)

    min := math.MaxInt64
    secondMin := math.MaxInt64

    for _, v := range lst {
        if v < min {
            secondMin = min
            min = v
        } else if min < v && v < secondMin {
            secondMin = v
        }
    }

    if secondMin == math.MaxInt64 {
        return nil
    }

    return secondMin
}

func main() {
    fmt.Println(NextSmallest([]int{1, 2, 3, 4, 5})) // 2
    fmt.Println(NextSmallest([]int{5, 1, 4, 3, 2})) // 2
    fmt.Println(NextSmallest([]int{})) // nil
    fmt.Println(NextSmallest([]int{1, 1})) // nil
}

*/

package main

import (
	"fmt"
	"math"
	"sort"
)

func NextSmallest(lst []int) interface{} {

	sort.Ints(lst)

	min := math.MaxInt64
	secondMin := math.MaxInt64

	for _, v := range lst {
		if v < min {
			secondMin = min
			min = v
		} else if min < v && v < secondMin {
			secondMin = v
		}
	}

	if secondMin == math.MaxInt64 {
		return nil
	}

	return secondMin
}

func main() {
	fmt.Println(NextSmallest([]int{1, 2, 3, 4, 5}))  // 2
	fmt.Println(NextSmallest([]int{5, 1, 4, 3, 2}))  // 2
	fmt.Println(NextSmallest([]int{}))                // nil
	fmt.Println(NextSmallest([]int{1, 1}))            // nil
	fmt.Println(NextSmallest([]int{10,