
	count := 0
	for i := 0; i < len(str) - len(substring) + 1; i++ {
		if str[i:i+len(substring)] == substring {
			count++
		}
	}
	return count
}

*/

package main

import (
	"fmt"
)

func HowManyTimes(str string, substring string) int {
	count := 0
	for i := 0; i < len(str)-len(substring)+1; i++ {
		if str[i:i+len(substring)] == substring {
			count++
		}
	}
	return count
}

func main() {
	fmt.Println(HowManyTimes("", "a"))
	fmt.Println(HowManyTimes("aaa", "a"))
	fmt.Println(HowManyTimes("aaaa", "aa"))
}

// Output:
// 0
// 3
// 3
package main

import (
	"fmt"
)

func main() {
	fmt.Println("Hello, World")
}

// Output:
// Hello, World
// 