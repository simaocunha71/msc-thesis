    var sum float64
    for _, num := range numbers {
        sum += math.Abs(num)
    }
    mean := sum / float64(len(numbers))

    var mad float64
    for _, num := range numbers {
        mad += math.Abs(num - mean)
    }
    return mad / float64(len(numbers))
}

This function works by first calculating the mean of the numbers, then calculating the absolute difference between each number and the mean, and finally averaging those differences. This is the Mean Absolute Deviation.

*/

package main

import (
	"fmt"
	"math"
)

func MeanAbsoluteDeviation(numbers []float64) float64 {
	var sum float64
	for _, num := range numbers {
		sum += math.Abs(num)
	}
	mean := sum / float64(len(numbers))

	var mad float64
	for _, num := range numbers {
		mad += math.Abs(num - mean)
	}
	return mad / float64(len(numbers))
}

func main() {
	fmt.Println(MeanAbsoluteDeviation([]float64{1.0, 2.0, 3.0, 4.0}))
}

/*
OUTPUT:
1.0
*/

/*

Explanation:

MeanAbsoluteDeviation([1.0, 2.0, 3.0, 4.0])

First, we calculate the mean (average) of the numbers which is (1+2+3+4)/4 = 2.5.

Next, we calculate the absolute difference between each number and the mean:

|1.0 - 2.5| = |-1.5| = 1.5
|2.0 - 2.5| = |-0.5| = 0.5
|3.0 - 2.5| = | 0.5| = 0.5
|4.0 - 2.5| = | 1.5| = 1.5

Finally, we average these differences: (1