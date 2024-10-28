
	var closest [2]float64
	minDiff := math.MaxFloat64

	for i := 0; i < len(numbers); i++ {
		for j := i + 1; j < len(numbers); j++ {
			if diff := math.Abs(numbers[i] - numbers[j]); diff < minDiff {
				minDiff = diff
				closest[0], closest[1] = numbers[i], numbers[j]
			}
		}
	}

	return closest
}



*/

package main

import (
	"fmt"
	"math"
)

func FindClosestElements(numbers []float64) [2]float64 {
	var closest [2]float64
	minDiff := math.MaxFloat64

	for i := 0; i < len(numbers); i++ {
		for j := i + 1; j < len(numbers); j++ {
			if diff := math.Abs(numbers[i] - numbers[j]); diff < minDiff {
				minDiff = diff
				closest[0], closest[1] = numbers[i], numbers[j]
			}
		}
	}

	return closest
}

func main() {
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.2})) // Expected: [2.0, 2.2]
	fmt.Println(FindClosestElements([]float64{1.0, 2.0, 3.0, 4.0, 5.0, 2.0})) // Expected: [2.0, 2.0]
}
package main

import (
	"fmt"
	"math"
)

func FindClosestElements(numbers []float64) [2]float64 {
	minDiff := math.MaxFloat64
	closest := [2]float64{}
	for i, num1 := range numbers {
		for _,