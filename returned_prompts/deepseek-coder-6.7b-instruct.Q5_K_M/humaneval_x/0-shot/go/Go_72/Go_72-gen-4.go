
// Write your code here

}

*/

import "fmt"

func WillItFly(q []int, w int) bool {
	sum := 0
	for _, num := range q {
		sum += num
	}
	if sum > w {
		return false
	}

	start := 0
	end := len(q) - 1
	for start < end {
		if q[start] != q[end] {
			return false
		}
		start++
		end--
	}
	return true
}

func main() {
	fmt.Println(WillItFly([]int{1, 2}, 5))     // false
	fmt.Println(WillItFly([]int{3, 2, 3}, 1))  // false
	fmt.Println(WillItFly([]int{3, 2, 3}, 9))  // true
	fmt.Println(WillItFly([]int{3}, 5))  // true
}

// The function WillItFly checks if the given slice q is a palindrome and the sum of its elements is less than or equal to the maximum possible weight w. If both conditions are met, it returns true. Otherwise, it returns false.
















































































































































































































