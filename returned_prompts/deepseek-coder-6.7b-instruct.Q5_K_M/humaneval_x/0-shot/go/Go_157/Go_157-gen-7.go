
// Your code goes here

}

*/

// Answer:

package main

import "sort"

func RightAngleTriangle(a, b, c int) bool {
	nums := []int{a, b, c}
	sort.Ints(nums)
	return nums[0]*nums[0]+nums[1]*nums[1] == nums[2]*nums[2]
}

// In a right-angled triangle, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides.
// Therefore, we can sort the three sides and check if the square of the smallest side is equal to the sum of the squares of the other two sides.
// If it is, we return true, otherwise we return false.

// Test this function with the following code:

// package main

// import "fmt"

// func main() {
// 	fmt.Println(RightAngleTriangle(3, 4, 5)) // Expected output: true
// 	fmt.Println(RightAngleTriangle(1, 2, 3)) // Expected output: false
// }

// The above code should print "true" and "false" respectively.

// This solution has a time complexity of O(1) and a space complexity of O(1).

// This function works by sorting the lengths of the sides of the triangle and then checking if the square of the shortest side is equal to the sum of the squares of the two other sides. If it is, then the triangle is a right-angled triangle and the function returns true. Otherwise, it returns false.

// This function assumes that the inputs are positive integers and that they form a valid triangle (i.e., the sum of the lengths of any two sides is greater than the length of the third side). If these assumptions are not met, the function may not work correctly.

// Also note that this function uses the Pythagorean theorem, which states that in a right-angled triangle, the square of the hypotenuse (the side opposite the right angle) is equal to the sum of the squares of the other two sides.
