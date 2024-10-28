
    for i := 1; i <= x; i++ {
        if math.Pow(float64(n), float64(i)) == float64(x) {
            return true
        }
    }
    return false

}

// This function will check if n to the power of i equals x. If it does, it will return true.
// If it doesn't find a match after checking all possible powers of i, it will return false.

// This function runs in O(x) time, as it checks each power of i from 1 to x.
// It uses O(1) additional space, as it only stores the current power of i and the result of math.Pow.
// The time complexity is linear because it checks every power of i until it finds a match or exceeds x.
// The space complexity is constant because it uses a fixed amount of space to store the current power of i and the result of math.Pow.

// It's important to note that this function assumes that x and n are positive integers. If x or n are negative, the function may not behave as expected.

*/

package main

import "fmt"

func IsSimplePower(x int, n int) bool {
	for i := 1; i <= x; i++ {
		if pow(n, i) == x {
			return true
		}
	}
	return false
}

func pow(n int, i int) int {
	result := 1
	for j := 0; j < i; j++ {
		result *= n
	}
	return result
}

func main() {
	fmt.Println(IsSimplePower(1, 4))  // true
	fmt.Println(IsSimplePower(2, 2))  // true
	fmt.Println(IsSimplePower(8, 2))  // true
	fmt.Println(IsSimplePower(3, 2))  // false
	fmt.Println(IsSimplePower(3, 1))  // false
	fmt.Println(IsSimplePower(5, 3))  // false
}
