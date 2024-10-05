
```go
func RemoveDuplicates(numbers []int) []int {
    uniqueNumbers := make([]int, 0)
    numberCount := make(map[int]int)

    for _, num := range numbers {
        numberCount[num]++
    }

    for _, num := range numbers {
        if numberCount[num] == 1 {
            uniqueNumbers = append(uniqueNumbers, num)
        }
    }

    return uniqueNumbers
}
```

Explanation:

We first create a map to count the occurrence of each number in the input list. Then we iterate over the original list again, and if a number occurs only once in the map, we add it to the result list. This keeps the order of elements as they appeared in the original list.

This solution has a time complexity of O(n) and a space complexity of O(n), where n is the length of the input list.

Please note that this solution assumes that the input list contains only integers and does not contain any negative numbers. If these assumptions are not valid, the solution might not work correctly.
*/

package main

import (
	"fmt"
)

func RemoveDuplicates(numbers []int) []int {
	uniqueNumbers := make([]int, 0)
	numberCount := make(map[int]int)

	for _, num := range numbers {
		numberCount[num]++
	}

	for _, num := range numbers {
		if numberCount[num] == 1 {
			uniqueNumbers = append(uniqueNumbers, num)
		}
	}

	return uniqueNumbers
}

func main() {
	fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4})) // Output: [1 3 4]
}

```

This function works by creating a map to count the occurrences of each number in the input list. It then iterates over the original list again, and for each number, if it occurs only once in the map, it is added to the result list. This keeps the order of elements as they appeared in the original list. The time