
	positive := []int{}

	for _, v := range l {
		if v > 0 {
			positive = append(positive, v)
		}
	}
	return positive
}

func main() {
	fmt.Println(GetPositive([]int{-1, 2, -4, 5, 6}))
	fmt.Println(GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
}

*/

package main

import "fmt"

func GetPositive(l []int) []int {
	positive := []int{}

	for _, v := range l {
		if v > 0 {
			positive = append(positive, v)
		}
	}
	return positive
}

func main() {
	fmt.Println(GetPositive([]int{-1, 2, -4, 5, 6}))
	fmt.Println(GetPositive([]int{5, 3, -5, 2, -3, 3, 9, 0, 123, 1, -10}))
}
package main

import "fmt"

func main() {
	word := "Hello, World!"
	fmt.Println(word)

	change := "Hello, Universe!"
	fmt.Println(change)
}
package main

import (
	"fmt"
	"os"
)

// 