    var evenLst []string
    for _, word := range lst {
        if len(word) % 2 == 0 {
            evenLst = append(evenLst, word)
        }
    }

    sort.Slice(evenLst, func(i, j int) bool {
        if len(evenLst[i]) == len(evenLst[j]) {
            return evenLst[i] < evenLst[j]
        }
        return len(evenLst[i]) < len(evenLst[j])
    })

    return evenLst
}

The function works by first creating a new slice `evenLst` that only includes the strings from the input slice `lst` that have even lengths. It then sorts this slice in ascending order of length and, if two strings have the same length, in alphabetical order. The sorted slice is then returned.


This code is written in Go and it takes a slice of strings as input and returns a slice of strings as output. It uses the `sort` package in Go to sort the slice. The `sort.Slice` function is used to sort the slice in place, and a custom comparison function is provided to sort the slice by length and then alphabetically if the lengths are the same. The `append` function is used to create the new slice of even length strings.


The time complexity of this code is O(n log n) because of the sorting operation. The space complexity is O(n) because we are creating a new slice to hold the even length strings.


Note: This code assumes that all words will have the same length. If this is not the case, you would need to modify the code to handle words of varying lengths.
*/

package main

import (
	"fmt"
	"sort"
)

func SortedListSum(lst []string) []string {
	var evenLst []string
	for _, word := range lst {
		if len(word)%2 == 0 {
			evenLst = append(evenLst, word)
		}
	}

	sort.Slice(evenLst, func(i, j int) bool {
		if len(evenLst[i