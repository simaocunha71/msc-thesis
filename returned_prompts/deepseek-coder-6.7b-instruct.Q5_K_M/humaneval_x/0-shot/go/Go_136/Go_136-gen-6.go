
	var maxNeg, minPos *int = nil, nil

	for _, v := range lst {
		if v > 0 {
			if minPos == nil || v < *minPos {
				minPos = &v
			}
		} else if v < 0 {
			if maxNeg == nil || v > *maxNeg {
				maxNeg = &v
			}
		}
	}

	return [2]interface{}{maxNeg, minPos}
}
*/

import "fmt"

func main() {

	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7}))
	fmt.Println(LargestSmallestIntegers([]int{}))
	fmt.Println(LargestSmallestIntegers([]int{0}))

}

func LargestSmallestIntegers(lst []int) [2]interface{} {

	var maxNeg, minPos *int = nil, nil

	for _, v := range lst {
		if v > 0 {
			if minPos == nil || v < *minPos {
				minPos = &v
			}
		} else if v < 0 {
			if maxNeg == nil || v > *maxNeg {
				maxNeg = &v
			}
		}
	}

	return [2]interface{}{maxNeg, minPos}
}
package main

import (
	"fmt"
	"strings"
)

/*
