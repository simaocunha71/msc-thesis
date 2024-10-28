package main

import (
	"fmt"
	"sort"
)

func main() {
	fmt.Println(Common([]int{1, 4, 3, 34, 653, 2, 5}, []int{5, 7, 1, 5, 9, 653, 121}))
	fmt.Println(Common([]int{5, 3, 2, 8}, []int{3, 2}))
}

func Common(l1 []int, l2 []int) []int {
	m := make(map[int]bool)
	var res []int

	for _, v := range l1 {
		m[v] = true
	}

	for _, v := range l2 {
		if _, ok := m[v]; ok {
			res = append(res, v)
			delete(m, v)
		}
	}

	sort.Ints(res)
	return res
}
