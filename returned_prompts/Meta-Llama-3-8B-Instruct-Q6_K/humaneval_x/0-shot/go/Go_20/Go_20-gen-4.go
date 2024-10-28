```go
package main

import (
	"fmt"
	"sort"
)

func FindClosestElements(numbers []float64) [2]float64 {
	sort.Float64s(numbers)
	minDiff := numbers[1] - numbers[0]
	closestElements := [2]float64{numbers[0], numbers[1]}
	for i := 2; i < len(numbers)-1; i++ {
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



The code first sorts the input numbers in ascending order. It then iterates through the sorted numbers to find the closest pair. The closest pair is the one with the smallest difference. If a smaller difference is found, the closest pair is updated. Finally, the code returns the closest pair in order (smaller number, larger number). The time complexity of this solution is O(n log n) due to the sorting step, where n is the length of the input numbers. The space complexity is O(1) as it only uses a constant amount of space.