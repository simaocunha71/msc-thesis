
    for i := range l {
        for j := i + 1; j < len(l); j++ {
            if l[i] + l[j] == 0 {
                return true
            }
        }
    }
    return false

}

*/

package main

import (
	"fmt"
)

func PairsSumToZero(l []int) bool {

	for i := range l {
		for j := i + 1; j < len(l); j++ {
			if l[i]+l[j] == 0 {
				return true
			}
		}
	}
	return false

}

func main() {
	fmt.Println(PairsSumToZero([]int{1, 3, 5, 0}))
	fmt.Println(PairsSumToZero([]int{1, 3, -2, 1}))
	fmt.Println(PairsSumToZero([]int{1, 2, 3, 7}))
	fmt.Println(PairsSumToZero([]int{2, 4, -5, 3, 5, 7}))
	fmt.Println(PairsSumToZero([]int{1}))
}
/*
