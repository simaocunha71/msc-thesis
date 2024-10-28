```go
package main

import (
	"fmt"
)

func Intersperse(numbers []int, delimeter int) []int {
	var result []int
	for i := 0; i < len(numbers); i++ {
		result = append(result, numbers[i])
		if i < len(numbers)-1 {
			result = append(result, delimeter)
		}
	}
	return result
}

func main() {
	fmt.Println(Intersperse([]int{}, 4))  // []
	fmt.Println(Intersperse([]int{1, 2, 3}, 4))  // [1, 4, 2, 4, 3]
}
```



This program defines a function `Intersperse` that takes a slice of integers `numbers` and an integer `delimeter` as input, and returns a new slice of integers where `delimeter` is inserted between every two consecutive elements of `numbers`.

In the `main` function, we call `Intersperse` with an empty slice and a non-empty slice, and print the results. The first call returns an empty slice, and the second call returns a slice where `4` is inserted between every two consecutive elements of `[1, 2, 3]`.

The `Intersperse` function uses a for loop to iterate over the input slice `numbers`. For each element, it appends the element to the result slice `result`. If the current index `i` is less than the length of `numbers` minus one, it appends `delimeter` to `result`. This ensures that `delimeter` is inserted between every two consecutive elements.

The time complexity of this function is O(n), where n is the length of the input slice `numbers`. The space complexity is also O(n), as we create a new slice `result` that may be larger than the input slice.