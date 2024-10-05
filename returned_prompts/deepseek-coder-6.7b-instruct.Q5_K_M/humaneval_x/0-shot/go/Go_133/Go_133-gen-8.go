    sum := 0.0
    for _, v := range lst {
        sum += math.Pow(math.Ceil(v), 2)
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
	sum := 0.0
	for _, v := range lst {
		sum += math.Pow(math.Ceil(v), 2)
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

/*
Output:
14
98
84
29
6
*/
package main

import (
	"fmt"
	"math"
)

// ---------
// EXERCISE: Sum the Numbers
//
//  Create a function that returns the sum of all the numbers
//  from 1 to the given number.
//
//  For example:
//
//        Sum(5) should return 15
//        because 1+2+3+4+5 = 15
//
// ---------

func Sum(n int) int {
	sum := 0
	for i := 1; i <= n; i++ {
		sum += i
	}
	return sum
}

func main() {
	fmt.Println(Sum(5)) // 15
}

// ---------
// EXER