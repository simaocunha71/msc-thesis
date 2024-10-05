
    sum := 0
    for i, v := range lst {
        if i % 2 != 0 && v % 2 == 0 {
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

func Add(lst []int) int {
	sum := 0
	for i, v := range lst {
		if i%2 != 0 && v%2 == 0 {
			sum += v
		}
	}
	return sum
}

func main() {
	fmt.Println(Add([]int{4, 2, 6, 7})) // 2
}
/*

