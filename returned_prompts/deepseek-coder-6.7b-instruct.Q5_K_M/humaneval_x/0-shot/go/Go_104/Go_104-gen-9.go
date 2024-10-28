    var res []int
    m := make(map[int]bool)

    for _, num := range x {
        if !hasEvenDigit(num) {
            if _, ok := m[num]; !ok {
                res = append(res, num)
                m[num] = true
            }
        }
    }

    sort.Ints(res)
    return res
}

func hasEvenDigit(n int) bool {
    for n > 0 {
        if (n%10)%2 == 0 {
            return true
        }
        n /= 10
    }
    return false
}

The function hasEvenDigit checks if a number contains an even digit or not,
and UniqueDigits uses this function to filter out numbers that contains
an even digit. If a number has no even digit, it is added to the result list
and marked in a map to avoid duplicates. Finally, the result list is sorted
and returned.

The time complexity of this program is O(n log n) because of the sorting operation,
and the space complexity is O(n) for storing the result list and the map.

The function hasEvenDigit works by taking the remainder of the number divided by 10
(which gives the last digit), and checking if it is even. If it is, the function
returns true. The function repeats this process by integer division of the number
by 10, removing the last digit until there are no digits left. If no even digit
is found, the function returns false.
*/
package main

import (
	"fmt"
)

func UniqueDigits(x []int) []int {
	var res []int
	m := make(map[int]bool)

	for _, num := range x {
		if !hasEvenDigit(num) {
			if _, ok := m[num]; !ok {
				res = append(res, num)
				m[num] = true
			}
		}
	}

	sort.Ints(res)
	return res
}

func hasEvenDigit(n int) bool {
	for n > 0 {
		if (n%