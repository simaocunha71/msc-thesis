    var res []int

    for _, num := range x {
        if hasNoEvenDigit(num) {
            res = append(res, num)
        }
    }

    sort.Ints(res)

    return res
}

func hasNoEvenDigit(num int) bool {

    for num > 0 {
        digit := num % 10
        if digit % 2 == 0 {
            return false
        }
        num /= 10
    }

    return true
}

This function works by iterating over each number in the input list x, and checking whether it has an even digit. If it does not, the number is appended to the result list. Finally, the result list is sorted in ascending order before being returned.
*/

package main

import (
	"fmt"
	"sort"
	"strconv"
)

func UniqueDigits(x []int) []int {
	var res []int

	for _, num := range x {
		if hasNoEvenDigit(num) {
			res = append(res, num)
		}
	}

	sort.Ints(res)

	return res
}

func hasNoEvenDigit(num int) bool {
	for num > 0 {
		digit := num % 10
		if digit%2 == 0 {
			return false
		}
		num /= 10
	}

	return true
}

func main() {
	fmt.Println(UniqueDigits([]int{15, 33, 1422, 1}))       // [1, 15, 33]
	fmt.Println(UniqueDigits([]int{152, 323, 1422, 10}))    // []
	fmt.Println(UniqueDigits([]int{89, 22, 110, 105, 123})) // [89, 105, 123]
}
