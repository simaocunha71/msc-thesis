
func GetPositive(l []int) []int {
    var result []int
    for _, v := range l {
        if v > 0 {
            result = append(result, v)
        }
    }
    return result
}

*/

import "fmt"

// GetPositive returns only positive numbers in the list
func GetPositive(l []int) []int {
	var result []int
	for _, v := range l {
		if v > 0 {
			result = append(result, v)
		}
	}
	return result
}

func main() {
	fmt.Println(GetPositive([]int{-1, 2, -4, 5, 6}))
	fmt.Println(GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
}
package main

import (
	"fmt"
	"strings"
)

/*

