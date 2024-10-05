    return int(math.Pow(2, float64(n-1)))
}

func main() {
    fmt.Println(StartsOneEnds(3))
}
*/

import (
	"fmt"
	"math"
)

// Given a positive integer n, return the count of the numbers of n-digit
// positive integers that start or end with 1.
func StartsOneEnds(n int) int {
	return int(math.Pow(2, float64(n-1)))
}

func main() {
	fmt.Println(StartsOneEnds(3))
}

/*
