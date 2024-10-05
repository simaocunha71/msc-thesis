
  var inc bool = true
  var dec bool = true

B:

  for i := 0; i < len(l)-1; i++ {
    if l[i] > l[i+1] {
      inc = false
    }
    if l[i] < l[i+1] {
      dec = false
    }
  }

C:

  return inc || dec
}

*/

package main

import (
	"fmt"
)

func Monotonic(l []int) bool {

	var inc bool = true
	var dec bool = true

	for i := 0; i < len(l)-1; i++ {
		if l[i] > l[i+1] {
			inc = false
		}
		if l[i] < l[i+1] {
			dec = false
		}
	}

	return inc || dec
}

func main() {
	fmt.Println(Monotonic([]int{1, 2, 4, 20}))      // true
	fmt.Println(Monotonic([]int{1, 20, 4, 10}))     // false
	fmt.Println(Monotonic([]int{4, 1, 0, -10}))     // true
	fmt.Println(Monotonic([]int{1, 1, 1, 1}))       // true
	fmt.Println(Monotonic([]int{1, 2, 2, 4}))       // true
	fmt.Println(Monotonic([]int{4, 3, 2, 1}))       // true
	fmt.Println(Monotonic([]int{1, 20, 20, 100}))   // true
	fmt.Println(Monotonic([]int{100, 20, 20, 1}))   // true
	fmt.Println(Monotonic([]int{100, 100, 100, 100})) // true
	fmt.Println(Monotonic([]int{