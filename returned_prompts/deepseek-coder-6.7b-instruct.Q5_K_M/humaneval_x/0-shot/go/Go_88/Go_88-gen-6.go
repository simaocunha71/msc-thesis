
import "sort"

func SortArray(array []int) []int {
    if len(array) <= 1 {
        return array
    }
    sorted := append([]int(nil), array...)
    sort.Ints(sorted)
    if (sorted[0]+sorted[len(sorted)-1])%2 == 1 {
        return sorted
    }
    for i, j := 0, len(sorted)-1; i < j; i, j = i+1, j-1 {
        sorted[i], sorted[j] = sorted[j], sorted[i]
    }
    return sorted
}

func main() {
    fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5}))         // [0, 1, 2, 3, 4, 5]
    fmt.Println(SortArray([]int{2, 4, 3, 0, 1, 5, 6}))       // [6, 5, 4, 3, 2, 1, 0]
}
*/

package main

import (
	"fmt"
	"sort"
)

func SortArray(array []int) []int {
	if len(array) <= 1 {
		return array
	}
	sorted := append([]int(nil), array...)
	sort.Ints(sorted)
	if (sorted[0]+sorted[len(sorted)-1])%