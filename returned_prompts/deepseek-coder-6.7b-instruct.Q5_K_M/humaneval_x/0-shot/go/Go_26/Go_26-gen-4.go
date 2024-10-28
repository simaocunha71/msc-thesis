
    result := make([]int, 0, len(numbers))
    counter := make(map[int]int)

    for _, num := range numbers {
        if counter[num] == 0 {
            counter[num]++
            result = append(result, num)
        } else {
            counter[num]++
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
	result := make([]int, 0, len(numbers))
	counter := make(map[int]int)

	for _, num := range numbers {
		if counter[num] == 0 {
			counter[num]++
			result = append(result, num)
		} else {
			counter[num]++
		}
	}

	return result
}

func main() {
	fmt.Println(RemoveDuplicates([]int{1, 2, 3, 2, 4}))
}
/*
