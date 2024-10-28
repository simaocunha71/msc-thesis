    var total float64
    for _, v := range lst {
        total += math.Pow(math.Ceil(v), 2)
    }
    return int(total)
}

*/

package main

import (
	"fmt"
	"math"
)

func SumSquares(lst []float64) int {
	var total float64
	for _, v := range lst {
		total += math.Pow(math.Ceil(v), 2)
	}
	return int(total)
}

func main() {
	fmt.Println(SumSquares([]float64{1, 2, 3}))         // 14
	fmt.Println(SumSquares([]float64{1, 4, 9}))         // 98
	fmt.Println(SumSquares([]float64{1, 3, 5, 7}))      // 84
	fmt.Println(SumSquares([]float64{1.4, 4.2, 0}))      // 29
	fmt.Println(SumSquares([]float64{-2.4, 1, 1}))      // 6
}

/*
Test Result:
14
98
84
29
6
*/
/*
