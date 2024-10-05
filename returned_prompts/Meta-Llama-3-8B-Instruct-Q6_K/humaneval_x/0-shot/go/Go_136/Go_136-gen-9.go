```go
package main

import (
	"fmt"
	"math"
)

func LargestSmallestIntegers(lst []int) [2]interface{} {
	var maxNegative, minPositive interface{}
	var foundNegative, foundPositive bool

	for _, v := range lst {
		if v < 0 {
			if !foundNegative {
				maxNegative = v
				foundNegative = true
			} else if v > math.Abs(float64(maxNegative.(int))) {
				maxNegative = v
			}
		} else if v > 0 {
			if !foundPositive {
				minPositive = v
				foundPositive = true
			} else if v < minPositive.(int) {
				minPositive = v
			}
		}
	}

	if !foundNegative && !foundPositive {
		return [2]interface{}{nil, nil}
	}

	if !foundNegative {
		return [2]interface{}{nil, minPositive}
	}

	if !foundPositive {
		return [2]interface{}{maxNegative, nil}
	}

	return [2]interface{}{maxNegative, minPositive}
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7}))  // (nil, 1)
	fmt.Println(LargestSmallestIntegers([]int{}))             // (nil, nil)
	fmt.Println(LargestSmallestIntegers([]int{0}))            // (nil, nil)
}
```
The function `LargestSmallestIntegers` iterates over the list `lst`, keeping track of the maximum negative and minimum positive integers found. If no negative or positive integers are found, it returns `(nil, nil)`. If only one type of integer is found, it returns `(nil, maxNegative)` or `(maxNegative, nil)` accordingly. Otherwise, it returns the maximum negative and minimum positive integers found. The function is tested in the `main` function with the provided examples.