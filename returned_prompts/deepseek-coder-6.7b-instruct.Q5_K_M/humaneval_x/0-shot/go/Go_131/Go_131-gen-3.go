    s := strconv.Itoa(n)
    product := 1
    for _, c := range s {
        digit, _ := strconv.Atoi(string(c))
        if digit%2 != 0 {
            product *= digit
        }
    }
    if product == 1 {
        return 0
    }
    return product
}

*/

package main

import (
	"fmt"
	"strconv"
)

func Digits(n int) int {
	s := strconv.Itoa(n)
	product := 1
	for _, c := range s {
		digit, _ := strconv.Atoi(string(c))
		if digit%2 != 0 {
			product *= digit
		}
	}
	if product == 1 {
		return 0
	}
	return product
}

func main() {
	fmt.Println(Digits(1))
	fmt.Println(Digits(4))
	fmt.Println(Digits(235))
}
package main

import (
	"fmt"
	"strconv"
)

/*
