sort.Slice(arr, func(i, j int) bool {
        a, b := arr[i], arr[j]
        if a < 0 {
            a = -a
        }
        if b < 0 {
            b = -b
        }
        bi, bj := fmt.Sprintf("%b", a), fmt.Sprintf("%b", b)
        onesi, onesj := 0, 0
        for _, v := range bi {
            if v == '1' {
                onesi++
            }
        }
        for _, v := range bj {
            if v == '1' {
                onesj++
            }
        }
        if onesi == onesj {
            return a < b
        }
        return onesi < onesj
    })
    return arr
}

*/

package main

import (
	"fmt"
	"sort"
	"strings"
)

func SortArray(arr []int) []int {
	sort.Slice(arr, func(i, j int) bool {
		a, b := arr[i], arr[j]
		bi, bj := fmt.Sprintf("%b", a), fmt.Sprintf("%b", b)
		onesi, onesj := strings.Count(bi, "1"), strings.Count(bj, "1")
		if onesi == onesj {
			return a < b
		}
		return onesi < onesj
	})
	return arr
}

func main() {
	fmt.Println(SortArray([]int{1, 5, 2, 3, 4}))
	fmt.Println(SortArray([]int{-2, -3, -4, -5, -6}))
	fmt.Println(SortArray([]int{1, 0, 2, 3, 4}))
}

/*
func main() {
	fmt.Println(SortArray([]int{1, 5, 2, 3, 4}))
	fmt.Println(SortArray([]int{-2, -3, -4, -5, -6}))