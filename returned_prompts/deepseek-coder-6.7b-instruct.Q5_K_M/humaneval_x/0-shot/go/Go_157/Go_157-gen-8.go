
// Sort the sides in ascending order
sort.Ints([]int{a, b, c})

B:

// Check if the square of the largest side is equal to the sum of the squares
// of the other two sides
return a*a+b*b == c*c
}

*/

import (
	"math"
	"sort"
)

func RightAngleTriangle(a, b, c int) bool {
	// Convert to float64 to perform math operations
	aFloat, bFloat, cFloat := float64(a), float64(b), float64(c)
	// Sort the sides in ascending order
	sides := []float64{aFloat, bFloat, cFloat}
	sort.Float64s(sides)
	// Check if the square of the largest side is equal to the sum of the squares
	// of the other two sides
	return math.Round(math.Pow(sides[2], 2)) == math.Round(math.Pow(sides[0], 2)+math.Pow(sides[1], 2))
}

func main() {
	fmt.Println(RightAngleTriangle(3, 4, 5)) // true
	fmt.Println(RightAngleTriangle(1, 2, 3)) // false
	fmt.Println(RightAngleTriangle(5, 12, 13)) // true
	fmt.Println(RightAngleTriangle(6, 8, 10)) // true
	fmt.Println(RightAngleTriangle(7, 24, 25)) // true
}

// Output:
// true
// false
// true
// true
// true

// Note: This function uses the Pythagorean theorem to determine if a triangle is right-angled.
// In a right-angled triangle, the square of the length of the hypotenuse (the side opposite the right angle)
// is equal to the sum of the squares of the lengths of the other two sides.
// We use math.Round to handle possible precision errors.
// We first sort the sides in ascending order to ensure