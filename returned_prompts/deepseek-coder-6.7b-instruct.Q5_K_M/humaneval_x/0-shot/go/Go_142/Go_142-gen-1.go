    sum := 0
    for i, v := range lst {
        if i % 3 == 0 {
            sum += int(math.Pow(float64(v), 2))
        } else if i % 4 == 0 {
            sum += int(math.Pow(float64(v), 3))
        } else {
            sum += v
        }
    }
    return sum
}

*/

package main

import (
	"fmt"
)

func SumSquares(lst []int) int {
	sum := 0
	for i, v := range lst {
		if i%3 == 0 {
			sum += v * v
		} else if i%4 == 0 {
			sum += v * v * v
		} else {
			sum += v
		}
	}
	return sum
}

func main() {
	fmt.Println(SumSquares([]int{1, 2, 3}))        // Output: 6
	fmt.Println(SumSquares([]int{}))               // Output: 0
	fmt.Println(SumSquares([]int{-1, -5, 2, -1, -5})) // Output: -126
}
package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(TwoSum([]int{1, 2, 3}, 4)) // Output: [0, 2]
	fmt.Println(TwoSum([]int{3, 2, 4}, 6)) // Output: [1, 2]
	fmt.Println(TwoSum([]int{3, 3}, 6))    // Output: [0, 1]
}

func TwoSum(numbers []int, target int) []int {
	m := make(map[int]int)
	for i, num := range numbers {
		if j, ok := m[target-num]; ok {
			return []int{j, i}
		}
		m[num] = i
	}
	return nil
