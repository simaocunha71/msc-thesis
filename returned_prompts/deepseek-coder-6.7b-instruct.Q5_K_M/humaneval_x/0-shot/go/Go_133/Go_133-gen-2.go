    var sum float64
    for _, num := range lst {
        sum += math.Pow(math.Ceil(num), 2)
    }

    return int(sum)
}

*/

package main

import (
	"fmt"
	"math"
)

func SumSquares(lst []float64) int {
	var sum float64
	for _, num := range lst {
		sum += math.Pow(math.Ceil(num), 2)
	}

	return int(sum)
}

func main() {
	fmt.Println(SumSquares([]float64{1, 2, 3}))       // 14
	fmt.Println(SumSquares([]float64{1, 4, 9}))       // 98
	fmt.Println(SumSquares([]float64{1, 3, 5, 7}))    // 84
	fmt.Println(SumSquares([]float64{1.4, 4.2, 0}))   // 29
	fmt.Println(SumSquares([]float64{-2.4, 1, 1}))    // 6
}

// Sample test:
// 1. The output should be 14 given lst = [1,2,3].
// 2. The output should be 98 given lst = [1,4,9].
// 3. The output should be 84 given lst = [1,3,5,7].
// 4. The output should be 29 given lst = [1.4,4.2,0].
// 5. The output should be 6 given lst = [-2.4,1,1].
// 6. The output should be 100 given lst = [10,10,10,10].
// 7. The output should be 117 given lst = [-5,-4,-3,-2,-1,0,1].
// 8. The output should be 28 given lst = [2.