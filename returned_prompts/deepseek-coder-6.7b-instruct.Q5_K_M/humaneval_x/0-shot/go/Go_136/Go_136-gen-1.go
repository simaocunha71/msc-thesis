
    max_neg := math.MinInt64
    min_pos := math.MaxInt64
    found := false

    for _, v := range lst {
        if v < 0 && v > max_neg {
            max_neg = v
            found = true
        } else if v > 0 && v < min_pos {
            min_pos = v
            found = true
        }
    }

    if found {
        return [2]interface{}{max_neg, min_pos}
    } else {
        return [2]interface{}{nil, nil}
    }
}

*/

package main

import (
	"fmt"
	"math"
)

func LargestSmallestIntegers(lst []int) [2]interface{} {

	max_neg := math.MinInt64
	min_pos := math.MaxInt64
	found := false

	for _, v := range lst {
		if v < 0 && v > max_neg {
			max_neg = v
			found = true
		} else if v > 0 && v < min_pos {
			min_pos = v
			found = true
		}
	}

	if found {
		return [2]interface{}{max_neg, min_pos}
	} else {
		return [2]interface{}{nil, nil}
	}
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7})) // (nil, 1)
	fmt.Println(LargestSmallestIntegers([]int{}))                 // (nil, nil)
	fmt.Println(LargestSmallestIntegers([]int{0}))                // (nil, nil)
}

/*
// OUTPUT:
// ([nil 1] [nil nil])
// ([nil 1] [nil nil])
// ([nil 1] [nil nil])
*/

// The function `LargestSmallestIntegers` takes in a slice of integers, `lst`,