
    m := make(map[int]int)
    var result []int

    for _, num := range numbers {
        if _, ok := m[num]; ok {
            continue
        }
        m[num]++
        result = append(result, num)
    }

    return result
}

*/

package main

import (
	"fmt"
)

func RemoveDuplicates(numbers []int) []int {

	m := make(map[int]int)
	var result []int

	for _, num := range numbers {
		if _, ok := m[num]; ok {
			continue
		}
		m[num]++
		result = append(result, num)
	}

	return result
}

func main() {

	numbers := []int{1, 2, 3, 2, 4}
	result := RemoveDuplicates(numbers)
	fmt.Println(result) // [1, 3, 4]

}
/*

