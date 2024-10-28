
    largest := math.MinInt64
    smallest := math.MaxInt64

    for _, v := range lst {
        if v < 0 && v > largest {
            largest = v
        }
        if v > 0 && v < smallest {
            smallest = v
        }
    }

    // If there is no negative or positive integers, return them as nil
    if largest == math.MinInt64 {
        largest = nil
    }
    if smallest == math.MaxInt64 {
        smallest = nil
    }

    return [2]interface{}{largest, smallest}
}

*/

package main

import (
	"fmt"
	"math"
)

func LargestSmallestIntegers(lst []int) [2]interface{} {

	largest := math.MinInt64
	smallest := math.MaxInt64

	for _, v := range lst {
		if v < 0 && v > largest {
			largest = v
		}
		if v > 0 && v < smallest {
			smallest = v
		}
	}

	// If there is no negative or positive integers, return them as nil
	if largest == math.MinInt64 {
		largest = nil
	}
	if smallest == math.MaxInt64 {
		smallest = nil
	}

	return [2]interface{}{largest, smallest}
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7})) //== (nil, 1)
	fmt.Println(LargestSmallestIntegers([]int{}))                 //== (nil, nil)
	fmt.Println(LargestSmallestIntegers([]int{0}))                //== (nil, nil)
}
package main

import (
	"fmt"
)

type Employee struct {
	Name   string
	Age    int
	Salary int
}

func (e Employee) GetEmployeeInfo() string {
	return fmt.