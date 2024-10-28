
// Define the minimum difference initially to be the maximum float64 value.
	minDiff := math.MaxFloat64
	var closestPair [2]float64

	// Loop over all pairs of numbers.
	for i := 0; i < len(numbers); i++ {
		for j := i + 1; j < len(numbers); j++ {

			// Calculate the absolute difference between the current pair.
			diff := math.Abs(numbers[i] - numbers[j])

			// If the difference is less than the current minimum difference, update the minimum difference and the closest pair.
			if diff < minDiff {
				minDiff = diff
				closestPair[0], closestPair[1] = numbers[i], numbers[j]

				// If the pair is found, break the loop.
				break
			}
		}
	}

	// Sort the closest pair in ascending order.
	sort.Float64s(closestPair[:])

	return closestPair
}

```

## Conclusion

The problem can be solved by using a brute-force approach to check all possible pairs of numbers and find the pair with the smallest difference. The time complexity is O(n^2) which is acceptable given the maximum length of the input list is 1000.

## Testing

Testing the function with the provided examples:

```go
package main

import (
	"fmt"
)

func main() {
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}))  // should print [2.0, 2.2]
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0}))  // should print [2.0, 2.0]
}
```

## Discussion

The problem is about finding two numbers in a list that are closest to each other. The brute-force solution is to check all pairs of numbers and find