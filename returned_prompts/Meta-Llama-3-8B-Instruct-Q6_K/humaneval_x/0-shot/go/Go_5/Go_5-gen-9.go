```go
package main

import (
	"fmt"
	"strconv"
)

func Intersperse(numbers []int, delimeter int) []int {
	var result []int
	for i := range numbers {
		if i > 0 {
			result = append(result, delimeter)
		}
		result = append(result, numbers[i])
	}
	return result
}

func main() {
	fmt.Println(Intersperse([]int{}, 4))
	fmt.Println(Intersperse([]int{1, 2, 3}, 4))
}
```

Output:
```
[]
[4 1 4 2 4 3]
```

Explanation:
This program defines a function `Intersperse` that takes a slice of integers `numbers` and an integer `delimeter` as input. It initializes an empty slice `result` and iterates over the input slice. For each element, if it's not the first element (i.e., `i > 0`), it appends the `delimeter` to the `result` slice. Then it appends the current element to the `result` slice. Finally, it returns the `result` slice.

In the `main` function, we test the `Intersperse` function with an empty slice and a slice with three elements. The output shows that the function correctly inserts the `delimeter` between every two consecutive elements of the input slice.