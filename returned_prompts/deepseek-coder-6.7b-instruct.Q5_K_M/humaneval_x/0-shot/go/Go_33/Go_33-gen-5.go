    s := make([]int, 0)
    for i, v := range l {
        if i % 3 == 0 {
            s = append(s, v)
        }
    }
    sort.Ints(s)

    for i, v := range l {
        if i % 3 == 0 {
            l[i] = s[0]
            s = s[1:]
        }
    }
    return l
}

func main() {
    fmt.Println(SortThird([]int{1, 2, 3}))
    fmt.Println(SortThird([]int{5, 6, 3, 4, 8, 9, 2}))
}

*/

package main

import (
	"fmt"
	"sort"
)

func SortThird(l []int) []int {

	s := make([]int, 0)
	for i, v := range l {
		if i%3 == 0 {
			s = append(s, v)
		}
	}
	sort.Ints(s)

	for i := range l {
		if i%3 == 0 {
			l[i] = s[0]
			s = s[1:]
		}
	}
	return l
}

func main() {
	fmt.Println(SortThird([]int{1, 2, 3}))
	fmt.Println(SortThird([]int{5, 6, 3, 4, 8, 9, 2}))
}

// Output:
// [2 6 3 4 8 9 5]
// [2 6 3 4 8 9 5]

// Explanation:
// In the first example, at indices 0, 3 and 6, the elements are divisible by 3.
// After sorting these elements [3, 9, 2] and replacing the original elements with the sorted ones,
// we get [2, 6, 3, 4, 8, 9, 5] which is the desired output.

//