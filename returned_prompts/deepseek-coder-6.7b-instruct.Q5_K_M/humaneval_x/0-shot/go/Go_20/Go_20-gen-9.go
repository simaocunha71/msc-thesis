
	sort.Float64s(numbers)

	min_diff := math.MaxFloat64
	var res [2]float64

	for i := 0; i < len(numbers) - 1; i++ {
		if diff := numbers[i+1] - numbers[i]; diff < min_diff {
			min_diff = diff
			res[0] = numbers[i]
			res[1] = numbers[i+1]
		}
	}

	return res
}

```

## Solution:

This solution uses the built-in `sort` package in Go to sort the `numbers` list. It then iterates through the sorted list to find the two elements with the smallest difference. 

The result is stored in the `res` array, which is returned at the end.

The time complexity of this solution is O(n log n) due to the sorting step, where n is the length of the `numbers` list.

The space complexity is O(1), as it uses a constant amount of space to store the result and the minimum difference.

It also handles the case where the two closest elements are the same by returning them in order.

## Test:

```go
package main

import (
	"fmt"
	"reflect"
)

func main() {
	fmt.Println(reflect.DeepEqual(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2}), [2]float64{2.0, 2.2}))
	fmt.Println(reflect.DeepEqual(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0}), [2]float64{2.0, 2.0}))
}
```

## Output:

```
true
true
```

## Explanation:

The `main` function tests the `FindClosestElements` function with the provided test cases. It uses the `DeepEqual` function from the `reflect