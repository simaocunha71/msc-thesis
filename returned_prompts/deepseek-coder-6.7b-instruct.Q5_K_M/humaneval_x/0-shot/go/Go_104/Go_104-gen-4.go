    var result []int

    for _, num := range x {
        if hasNoEvenDigits(num) {
            result = append(result, num)
        }
    }

    sort.Ints(result)
    return result
}

func hasNoEvenDigits(n int) bool {
    for n > 0 {
        if (n%10)%2 == 0 {
            return false
        }
        n /= 10
    }
    return true
}


func main() {
    fmt.Println(UniqueDigits([]int{15, 33, 1422, 1})) //[1, 15, 33]
    fmt.Println(UniqueDigits([]int{152, 323, 1422, 10})) // []
}

This code is a simple solution to the problem. First, it defines a function `hasNoEvenDigits` that checks if a number has any even digit. Then, the main function `UniqueDigits` uses this helper function to filter the numbers in the input list and append the ones that have no even digits to the result list. Finally, it sorts the result list and returns it.

The time complexity of this solution is O(n*m), where n is the number of elements in the input list and m is the number of digits in the largest number. The space complexity is O(n), as we need to store the result list.
*/

import (
	"fmt"
	"sort"
	"strconv"
)

func UniqueDigits(x []int) []int {
	var result []int

	for _, num := range x {
		if hasNoEvenDigits(num) {
			result = append(result, num)
		}
	}

	sort.Ints(result)
	return result
}

func hasNoEvenDigits(n int) bool {
	for _, digit := range strconv.Itoa(n) {
		num, _ := strconv.Atoi(string(digit))
		if num%2 == 0 {
			return false
		}
	}
	return