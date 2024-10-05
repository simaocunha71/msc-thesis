    s := strconv.Itoa(n)
    result := 1

B:
    for _, c := range s {
        digit, _ := strconv.Atoi(string(c))
        if digit%2 != 0 {
            result *= digit
        }
    }

C:
    if result == 1 {
        return 0
    }
    return result
}

func main() {
    fmt.Println(Digits(235))
}

*/

package main

import (
	"fmt"
	"strconv"
)

func Digits(n int) int {
	s := strconv.Itoa(n)
	result := 1

	for _, c := range s {
		digit, _ := strconv.Atoi(string(c))
		if digit%2 != 0 {
			result *= digit
		}
	}

	if result == 1 {
		return 0
	}

	return result
}

func main() {
	fmt.Println(Digits(235))
}
/*
