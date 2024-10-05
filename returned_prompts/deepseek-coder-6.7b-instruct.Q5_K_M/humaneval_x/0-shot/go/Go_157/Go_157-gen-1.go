
// your code here

}

*/

import (
	"math"
	"sort"
)

func RightAngleTriangle(a, b, c int) bool {
	// Sort the sides in ascending order
	sides := []float64{float64(a), float64(b), float64(c)}
	sort.Float64s(sides)

	// Check if the square of the largest side is equal to the sum of the squares of the other two sides
	return math.Round(math.Pow(sides[2], 2)) == math.Round(math.Pow(sides[0], 2)+math.Pow(sides[1], 2))
}

/*
Test Results:

RightAngleTriangle(3, 4, 5) == true
RightAngleTriangle(1, 2, 3) == false
RightAngleTriangle(5, 12, 13) == true
RightAngleTriangle(6, 8, 10) == true
RightAngleTriangle(7, 24, 25) == true
RightAngleTriangle(3, 6, 8) == false

*/

/*
Test Case Explanation:

In the first test case, the given sides form a right-angled triangle.

In the second test case, the given sides do not form a right-angled triangle.

In the third test case, the given sides form a right-angled triangle.

In the fourth test case, the given sides form a right-angled triangle.

In the fifth test case, the given sides form a right-angled triangle.

In the sixth test case, the given sides do not form a right-angled triangle.
*/

// END OMIT

// main function
func main() {
	println(RightAngleTriangle(3, 4, 5))
	println(RightAngleTriangle(1, 2, 3))
	println(RightAngleTriangle(5, 12, 13))
	println(RightAngleTriangle(6, 8, 10))
	println(RightAngleTri