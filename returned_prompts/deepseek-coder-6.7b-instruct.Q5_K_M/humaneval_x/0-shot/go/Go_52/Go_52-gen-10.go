
    // Write your code here

}

*/

package main

import "fmt"

func BelowThreshold(l []int, t int) bool {
	for _, v := range l {
		if v >= t {
			return false
		}
	}
	return true
}

func main() {
	fmt.Println(BelowThreshold([]int{1, 2, 4, 10}, 100)) // true
	fmt.Println(BelowThreshold([]int{1, 20, 4, 10}, 5))  // false
}
