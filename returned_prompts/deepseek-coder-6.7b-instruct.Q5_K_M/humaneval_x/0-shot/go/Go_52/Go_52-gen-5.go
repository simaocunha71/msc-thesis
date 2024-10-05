
for i := range l {

B:

if l[i] >= t {

C:

return false
}

D:

}

E:

return true
}

// F:

I tried to solve this problem by using a for loop to iterate over each element in the list and checking if the element is greater or equal to the threshold. If it is, I return false. If the loop finishes without returning, I return true.

*/

package main

import "fmt"

func BelowThreshold(l []int, t int) bool {
	for i := range l {
		if l[i] >= t {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(BelowThreshold([]int{1, 2, 4, 10}, 100)) // true
	fmt.Println(BelowThreshold([]int{1, 20, 4, 10}, 5))  // false
}
package main

import "fmt"

func main() {
	arr := []int{1, 2, 3, 4, 5}

	for i, v := range arr {
		fmt.Println(i, v)
	}

	// 0 1
	// 1 2
	// 2 3
	// 3 4
	// 4 5
}

// The range keyword in Go provides a convenient way to iterate over elements in a variety of data structures. When used with arrays or slices, it provides both the index and value of each element.

// In the loop above, i is the index of the current element, and v is its value. The loop continues until it has iterated over all elements in the array.

// In the code sample, we use range to iterate over an array of integers. The range keyword returns two values on each iteration. The first is the index, and the second is a copy of the element at that index.

// The range keyword can be used with other data structures in Go, such as maps and strings.

// The range keyword is a powerful tool for working with collections of data in Go.