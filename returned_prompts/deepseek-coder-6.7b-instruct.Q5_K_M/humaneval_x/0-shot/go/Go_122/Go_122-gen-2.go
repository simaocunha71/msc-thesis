    sum := 0
    for i := 0; i < k; i++ {
        if len(strconv.Itoa(arr[i])) <= 2 {
            sum += arr[i]
        }
    }
    return sum
}

The code works by iterating over the first k elements of the array and checking the number of digits in each element. If the number of digits is less than or equal to 2, it adds the element to the sum. The function finally returns the sum.
*/

package main

import (
	"fmt"
)

func AddElements(arr []int, k int) int {
	sum := 0
	for i := 0; i < k; i++ {
		if len(fmt.Sprintf("%d", arr[i])) <= 2 {
			sum += arr[i]
		}
	}
	return sum
}

func main() {
	arr := []int{111, 21, 3, 4000, 5, 6, 7, 8, 9}
	k := 4
	fmt.Println(AddElements(arr, k))
}

/*
In this program, the function `AddElements` calculates the sum of elements with at most two digits from the first k elements of the array `arr`.

In the main function, we test the `AddElements` function with the given array and k value. The result should be 24, which is the sum of 21 and 3.
*/
/*
