
// Add your code below:
sum := 0
for _, v := range q {
	sum += v
}
if sum > w {
	return false
}
return true
}

*/

package main

import (
	"fmt"
)

func WillItFly(q []int, w int) bool {
	sum := 0
	for _, v := range q {
		sum += v
	}
	if sum > w {
		return false
	}
	return true
}

func main() {
	fmt.Println(WillItFly([]int{1, 2}, 5))
	fmt.Println(WillItFly([]int{3, 2, 3}, 1))
	fmt.Println(WillItFly([]int{3, 2, 3}, 9))
	fmt.Println(WillItFly([]int{3}, 5))
}

// Output:
// false
// false
// true
// true
package main

import (
	"fmt"
	"math"
)

// Given an array of integers, write a function that returns the sum of the squares of the elements of the array.

// For example, given the array [1, 2, 3, 4], the function should return 30, because 1^2 + 2^2 + 3^2 + 4^2 = 1 + 4 + 9 + 16 = 30.

func SumOfSquares(numbers []int) int {
	sum := 0
	for _, number := range numbers {
		sum += int(math.Pow(float64(number), 2))
	}
	return sum
}

func main() {
	fmt.Println(SumOfSquares([]int{1, 2, 3, 4})) // Output: 30
}

// Explanation:
// The function works by iterating over each number in the given array. For each number, it calculates the square of the number using the math.Pow function, which takes a float64 and an exponent and returns the result as a float64. The result is then converted back