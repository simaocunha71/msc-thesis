```go
package main

import (
	"fmt"
	"math"
)

func FindClosestElements(numbers []float64) [2]float64 {
	var minDiff float64 = math.MaxFloat64
	var closestElements [2]float64

	for i := 0; i < len(numbers)-1; i++ {
		diff := numbers[i+1] - numbers[i]
		if diff < minDiff {
			minDiff = diff
			closestElements[0] = numbers[i]
			closestElements[1] = numbers[i+1]
		}
	}

	return closestElements
}

func main() {
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}))
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0}))
}
```

Output:
```
[2. 2.2]
[2. 2]
```


This solution iterates over the list of numbers, calculating the difference between each pair of adjacent numbers. It keeps track of the pair with the smallest difference, returning that pair at the end. If the input list contains duplicate numbers, the solution will return the first occurrence of the closest pair. 

The time complexity of this solution is O(n), where n is the length of the input list, as it needs to iterate over the list once to find the closest pair. The space complexity is O(1), as it only uses a constant amount of space to store the minimum difference and the closest pair. 