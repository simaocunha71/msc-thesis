
	sum := 0
	nums := []int{0, 0, 0}

	switch x := x.(type) {
	case int:
		nums[0] = x
		sum += x
	default:
		goto B
	}

	switch y := y.(type) {
	case int:
		nums[1] = y
		sum += y
	default:
		goto B
	}

	switch z := z.(type) {
	case int:
		nums[2] = z
		sum += z
	default:
		goto B
	}

	for _, n := range nums {
		if n == 0 {
			goto B
		}
	}

	for _, n := range nums {
		if n == sum-n {
			return true
		}
	}

B:
	return false
}

func main() {
    fmt.Println(AnyInt(5, 2, 7)) // ➞ true
    fmt.Println(AnyInt(3, 2, 2)) // ➞ false
    fmt.Println(AnyInt(3, -2, 1)) // ➞ true
    fmt.Println(AnyInt(3.6, -2.2, 2)) // ➞ false
}

*/

package main

import (
	"fmt"
)

func AnyInt(x, y, z interface{}) bool {
	sum := 0
	nums := []int{0, 0, 0}

	switch x := x.(type) {
	case int:
		nums[0] = x
		sum += x
	default:
		return false
	}

	switch y := y.(type) {
	case int:
		nums[1] = y
		sum += y
	default:
		return false
	}

	switch z := z.(type) {
	case int:
		nums[2] = z
		sum += z
	default:
		return false
	}

	for