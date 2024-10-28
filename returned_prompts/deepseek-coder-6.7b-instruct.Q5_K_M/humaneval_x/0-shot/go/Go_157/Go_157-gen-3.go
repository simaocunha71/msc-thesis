
// Your code here

}

*/

package main

import (
	"fmt"
	"sort"
)

func RightAngleTriangle(a, b, c int) bool {
	sides := []int{a, b, c}
	sort.Ints(sides)
	return sides[0]*sides[0]+sides[1]*sides[1] == sides[2]*sides[2]
}

func main() {
	fmt.Println(RightAngleTriangle(3, 4, 5)) // == true
	fmt.Println(RightAngleTriangle(1, 2, 3)) // == false
}

/*

