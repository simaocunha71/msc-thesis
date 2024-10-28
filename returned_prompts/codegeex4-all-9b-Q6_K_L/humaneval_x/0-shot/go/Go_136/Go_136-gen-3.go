You can solve this problem by using the following steps:

1. Initialize two variables, `maxNeg` and `minPos`, to `nil` and `-math.MaxInt32` respectively.
2. Iterate through the list and update `maxNeg` and `minPos` if a negative or positive integer is found respectively.
3. Return the tuple `(maxNeg, minPos)`.

Here is the solution in Go:

```go
package main

import (
	"fmt"
	"math"
)

func LargestSmallestIntegers(lst []int) (interface{}, interface{}) {
	maxNeg := nil
	minPos := nil
	for _, num := range lst {
		if num < 0 {
			if maxNeg == nil || num > maxNeg.(int) {
				maxNeg = num
			}
		} else if num > 0 {
			if minPos == nil || num < minPos.(int) {
				minPos = num
			}
		}
	}
	return maxNeg, minPos
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7})) // Output: (nil, 1)
	fmt.Println(LargestSmallestIntegers([]int{}))                // Output: (nil, nil)
	fmt.Println(LargestSmallestIntegers([]int{0}))               // Output: (nil, nil)
}
```

In this solution, we use the `interface{}` type to represent `nil` values. We initialize `maxNeg` and `minPos` to `nil` and `-math.MaxInt32` respectively. We iterate through the list and update `maxNeg` and `minPos` if a negative or positive integer is found respectively. Finally, we return the tuple `(maxNeg, minPos)`.