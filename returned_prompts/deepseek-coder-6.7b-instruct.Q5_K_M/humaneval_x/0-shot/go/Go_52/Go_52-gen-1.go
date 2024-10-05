
// iterate over the list
for i := range l {

  // if any number in the list is greater than or equal to the threshold, return false
  if l[i] >= t {
    return false
  }
}

// if none of the numbers in the list are greater than or equal to the threshold, return true
return true
}
*/

package main

import (
	"fmt"
)

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

import (
	"fmt"
)

func main() {
	fmt.Println(Fib(0)) // 0
	fmt.Println(Fib(1)) // 1
	fmt.Println(Fib(2)) // 1
	fmt.Println(Fib(3)) // 2
	fmt.Println(Fib(4)) // 3
	fmt.Println(Fib(5)) // 5
	fmt.Println(Fib(6)) // 8
}

// Fib returns the nth Fibonacci number.
func Fib(n int) int {
	if n <= 1 {
		return n
	}

	prev, next := 0, 1
	for i := 1; i < n; i++ {
		prev, next = next, prev+next
	}

	return next
}
package main

import (
	"fmt"
)

func main() {
	fmt.Println(IsPalindrome("racecar")) // true
	fmt.Println(IsPalindrome("hello"))   // false
	fmt.Println(IsPalindrome("a"))       // true
	fmt.