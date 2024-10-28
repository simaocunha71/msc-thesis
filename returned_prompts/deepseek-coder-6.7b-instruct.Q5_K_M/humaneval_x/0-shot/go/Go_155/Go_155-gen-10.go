    var res [2]int
    numStr := strconv.Itoa(num)

    for _, v := range numStr {
        digit, _ := strconv.Atoi(string(v))
        if digit % 2 == 0 {
            res[0]++
        } else {
            res[1]++
        }
    }
    return res
}

*/

package main

import (
	"fmt"
	"strconv"
)

func EvenOddCount(num int) [2]int {
	var res [2]int
	numStr := strconv.Itoa(num)

	for _, v := range numStr {
		digit, _ := strconv.Atoi(string(v))
		if digit%2 == 0 {
			res[0]++
		} else {
			res[1]++
		}
	}
	return res
}

func main() {
	fmt.Println(EvenOddCount(-12))
	fmt.Println(EvenOddCount(123))
}
/*
