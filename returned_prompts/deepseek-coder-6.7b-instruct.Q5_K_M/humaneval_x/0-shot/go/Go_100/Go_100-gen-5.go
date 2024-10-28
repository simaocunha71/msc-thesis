
    stones := make([]int, 0, n)
    for i := 0; i < n; i++ {
        if n%2 == 0 {
            stones = append(stones, n+2*i)
        } else {
            stones = append(stones, n+2*i)
        }
    }
    return stones
}

*/

// MakeAPile returns a list of the number of stones in each level of a pile of stones.
func MakeAPile(n int) []int {
	stones := make([]int, 0, n)
	for i := 0; i < n; i++ {
		if n%2 == 0 {
			stones = append(stones, n+2*i)
		} else {
			stones = append(stones, n+2*i)
		}
	}
	return stones
}

// The test function
func main() {
	fmt.Println(MakeAPile(3)) // [3 5 7]
}
package main

import (
	"fmt"
	"strings"
	"unicode"
)

/*
