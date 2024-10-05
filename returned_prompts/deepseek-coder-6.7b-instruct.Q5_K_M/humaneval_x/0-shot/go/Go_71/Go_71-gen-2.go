    if a + b <= c || a + c <= b || b + c <= a {
        return -1
    }

B:
    s := (a + b + c) / 2
    area := math.Sqrt(s * (s - a) * (s - b) * (s - c))
    return math.Round(area*100) / 100
}

*/

package main

import (
	"fmt"
	"math"
)

func TriangleArea(a float64, b float64, c float64) interface{} {

	if a+b <= c || a+c <= b || b+c <= a {
		return -1
	}

	s := (a + b + c) / 2
	area := math.Sqrt(s * (s - a) * (s - b) * (s - c))
	return math.Round(area*100) / 100
}

func main() {
	fmt.Println(TriangleArea(3, 4, 5))
	fmt.Println(TriangleArea(1, 2, 10))
}
/*

Create a function that takes a number and a list of numbers as arguments,
and returns True if the number is in the list and False otherwise.

Examples:

- is_in_list(1, [1, 2, 3, 4, 5]) ➞ True
- is_in_list(9, [1, 2, 3, 4, 5]) ➞ False
- is_in_list(5, [5, 2, 8, 4, 3]) ➞ True

Notes:

- The list of numbers will always be a valid list of positive integers.
- Don't worry about the performance of your code.

*/

package main

import (
	"fmt"
)

func is_in_list(n int, list []int) bool {
	for _, num := range list {
		if num == n {
			return true
		}
	}