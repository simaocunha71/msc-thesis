```go
package main

import (
	"fmt"
	"sort"
)

func RemoveDuplicates(numbers []int) []int {
	keys := make(map[int]bool)
	list := []int{}
	for _, value := range numbers {
		if _, valueExist := keys[value]; !valueExist {
			keys[value] = true
			list = append(list, value)
		}
	}
	sort.Ints(list)
	return list
}

func main() {
	numbers := []int{1, 2, 3, 2, 4}
	fmt.Println(RemoveDuplicates(numbers)) // Output: [1 2 3 4]
}
```
The function `RemoveDuplicates` takes a slice of integers as input and returns a new slice with the duplicates removed. It uses a map to keep track of the unique elements and a slice to store the result. It iterates over the input slice, and for each element, it checks if it's already in the map. If not, it adds it to the map and the result slice. Finally, it sorts the result slice to keep the original order. The `main` function demonstrates how to use this function. The output of the program is `[1 2 3 4]`, which is the input slice with the duplicates removed.