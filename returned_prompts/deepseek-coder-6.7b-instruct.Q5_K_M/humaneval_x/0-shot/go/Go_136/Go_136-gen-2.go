
    var largest, smallest interface{} = nil, nil

    for _, v := range lst {
        if v > 0 {
            if smallest == nil || v < smallest.(int) {
                smallest = v
            }
        } else if v < 0 {
            if largest == nil || v > largest.(int) {
                largest = v
            }
        }
    }

    return [2]interface{}{largest, smallest}
}

*/

func LargestSmallestIntegers(lst []int) [2]interface{} {

	var largest, smallest interface{} = nil, nil

	for _, v := range lst {
		if v > 0 {
			if smallest == nil || v < smallest.(int) {
				smallest = v
			}
		} else if v < 0 {
			if largest == nil || v > largest.(int) {
				largest = v
			}
		}
	}

	return [2]interface{}{largest, smallest}
}

func main() {
	fmt.Println(LargestSmallestIntegers([]int{2, 4, 1, 3, 5, 7})) // (nil, 1)
	fmt.Println(LargestSmallestIntegers([]int{}))                 // (nil, nil)
	fmt.Println(LargestSmallestIntegers([]int{0}))                // (nil, nil)
}
package main

import "fmt"

// 