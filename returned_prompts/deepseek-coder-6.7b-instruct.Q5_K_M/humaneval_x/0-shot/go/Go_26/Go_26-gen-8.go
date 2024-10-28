
    var result []int
    m := make(map[int]int)

    for _, num := range numbers {
        m[num]++
    }

    for _, num := range numbers {
        if m[num] == 1 {
            result = append(result, num)
        }
    }

    return result
}

*/

package main

import (
	"fmt"
)

func RemoveDuplicates(numbers []int) []int {

	var result []int
	m := make(map[int]int)

	for _, num := range numbers {
		m[num]++
	}

	for _, num := range numbers {
		if m[num] == 1 {
			result = append(result, num)
		}
	}

	return result
}

func main() {
	fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}

// [1, 3, 4]
// Output: [1, 3, 4]
// Explanation:
// After removing all the duplicates, the only numbers left are 1, 3, and 4. The order of the numbers in the output is the same as the order they occur in the input.
// Hence, the output is [1, 3, 4].
/*
