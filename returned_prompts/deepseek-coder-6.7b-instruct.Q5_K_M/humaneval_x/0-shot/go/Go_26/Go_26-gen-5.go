
	unique := make(map[int]struct{})
	result := make([]int, 0)

	for _, number := range numbers {
		if _, ok := unique[number]; !ok {
			unique[number] = struct{}{}
			result = append(result, number)
		}
	}
	return result
}

func main() {
	fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}
```

This function works by creating a map to keep track of the unique numbers it has encountered. For each number in the input slice, it checks if the number is already in the map. If it is not, it adds the number to the map and appends it to the result slice. This ensures that only the first occurrence of a number is kept, while the rest are removed.

The time complexity of this function is O(n) where n is the length of the input slice because it traverses the slice once. The space complexity is also O(n) because in the worst case, all elements in the input slice would be unique and the map would have to store n elements.

Please note that this function will work correctly if the input slice is sorted. If the input slice is not sorted, you may need to sort it first before using this function.
*/
package main

import (
	"fmt"
)

func RemoveDuplicates(numbers []int) []int {
	unique := make(map[int]struct{})
	result := make([]int, 0)

	for _, number := range numbers {
		if _, ok := unique[number]; !ok {
			unique[number] = struct{}{}
			result = append(result, number)
		}
	}
	return result
}

func main() {
	fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}
```

This function works by creating a map to keep track of the unique numbers it has encountered. For each number in the input slice, it checks if the number is already in the map. If it is not, it adds the number to the map and appends it