    sort.Ints(l)
    var r []int
    var last int
    for _, v := range l {
        if v != last {
            r = append(r, v)
            last = v
        }
    }
    return r
}

*/

package main

import (
	"fmt"
	"sort"
)

func Unique(l []int) []int {
	sort.Ints(l)
	var r []int
	var last int
	for _, v := range l {
		if v != last {
			r = append(r, v)
			last = v
		}
	}
	return r
}

func main() {
	data := []int{5, 3, 5, 2, 3, 3, 9, 0, 123}
	fmt.Println(Unique(data))
}
/*
