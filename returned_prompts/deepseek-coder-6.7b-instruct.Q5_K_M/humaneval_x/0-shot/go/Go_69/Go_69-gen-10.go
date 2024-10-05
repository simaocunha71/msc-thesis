
// we will count the frequency of each integer in the list using a map
// then we will iterate over the map in reverse order to find the greatest integer that has a frequency
// greater than or equal to the value of the integer itself

var frequencyMap = make(map[int]int)
var maxInt = -1

for _, value := range lst {
    frequencyMap[value]++
}

for i := len(lst); i > 0; i-- {
    if frequency, exists := frequencyMap[i]; exists && frequency >= i {
        maxInt = i
        break
    }
}

return maxInt

}

*/

package main

import "fmt"

func Search(lst []int) int {
	var frequencyMap = make(map[int]int)
	var maxInt = -1

	for _, value := range lst {
		frequencyMap[value]++
	}

	for i := len(lst); i > 0; i-- {
		if frequency, exists := frequencyMap[i]; exists && frequency >= i {
			maxInt = i
			break
		}
	}

	return maxInt
}

func main() {
	fmt.Println(Search([]int{4, 1, 2, 2, 3, 1})) // 2
	fmt.Println(Search([]int{1, 2, 2, 3, 3, 3, 4, 4, 4})) // 3
	fmt.Println(Search([]int{5, 5, 4, 4, 4})) // -1
}
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "hello world"
	str2 := "HELLO WORLD"
	str3 := "HeLlO wOrLd"

	fmt.Println(toUppercase(str))
	fmt.Println(toUppercase(str2))
	fmt.Println(toUppercase(str3))
}

func toUppercase(str string)