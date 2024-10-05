
// Create a function to check if a list is a palindrome
isPalindrome := func(q []int) bool {
    for i := 0; i < len(q)/2; i++ {
        if q[i] != q[len(q)-i-1] {
            return false
        }
    }
    return true
}

// Create a function to calculate the sum of the elements in the list
sum := func(q []int) int {
    sum := 0
    for _, v := range q {
        sum += v
    }
    return sum
}

// Check if the list is balanced and the sum is less than or equal the maximum possible weight
return isPalindrome(q) && sum(q) <= w

}


*/

package main

import (
	"fmt"
)

func main() {
	fmt.Println(WillItFly([]int{1, 2}, 5))
	fmt.Println(WillItFly([]int{3, 2, 3}, 1))
	fmt.Println(WillItFly([]int{3, 2, 3}, 9))
	fmt.Println(WillItFly([]int{3}, 5))
}

func WillItFly(q []int, w int) bool {

	isPalindrome := func(q []int) bool {
		for i := 0; i < len(q)/2; i++ {
			if q[i] != q[len(q)-i-1] {
				return false
			}
		}
		return true
	}

	sum := func(q []int) int {
		total := 0
		for _, v := range q {
			total += v
		}
		return total
	}

	return isPalindrome(q) && sum(q) <= w

}
package main

import (
	"fmt"
	"math"
)

// Given a number, return the number of ways to represent that number as a sum of two or more consecutive non-zero positive integers.
//