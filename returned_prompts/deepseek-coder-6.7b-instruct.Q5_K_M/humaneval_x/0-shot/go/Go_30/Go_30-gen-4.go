
    positive := make([]int, 0)
    for _, v := range l {
        if v > 0 {
            positive = append(positive, v)
        }
    }
    return positive
}

*/

func main() {
	l := []int{-1, 2, -4, 5, 6}
	fmt.Println(GetPositive(l))

	l2 := []int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}
	fmt.Println(GetPositive(l2))
}

func GetPositive(l []int) []int {
	positive := make([]int, 0)
	for _, v := range l {
		if v > 0 {
			positive = append(positive, v)
		}
	}
	return positive
}
/*
* Task 3: 
* Create a program that will return the maximum number in a list.
* The list can contain both positive and negative numbers.
* If the list is empty, return a message "The list is empty".
* 
* Note: You can use the sort package in Golang to solve this task.
*/

package main

import (
	"fmt"
	"sort"
)

func main() {
	list := []int{1, 3, 5, 7, 9, 2, 4, 6, 8, 10, -1, -3, -5, -7, -9, -2, -4, -6, -8, -10}
	max := findMax(list)
	fmt.Printf("The maximum number in the list is: %d\n", max)

	list2 := []int{}
	max2 := findMax(list2)
	fmt.Printf("The maximum number in the list is: %s\n", max2)
}

func findMax(list []int) interface{} {
	if len(list) == 0 {
		return "The list is empty"
	}

	sort.Int