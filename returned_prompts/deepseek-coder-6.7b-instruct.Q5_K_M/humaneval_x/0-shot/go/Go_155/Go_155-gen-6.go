     var countEven int = 0
     var countOdd int = 0
     strNum := strconv.Itoa(num)
     for _, c := range strNum {
         digit, _ := strconv.Atoi(string(c))
         if digit%2 == 0 {
             countEven++
         } else {
             countOdd++
         }
     }
     return [2]int{countEven, countOdd}
}

*/

package main

import (
	"fmt"
	"strconv"
)

func EvenOddCount(num int) [2]int {
	var countEven int = 0
	var countOdd int = 0
	strNum := strconv.Itoa(num)
	for _, c := range strNum {
		digit, _ := strconv.Atoi(string(c))
		if digit%2 == 0 {
			countEven++
		} else {
			countOdd++
		}
	}
	return [2]int{countEven, countOdd}
}

func main() {
	fmt.Println(EvenOddCount(-12)) // ==> [1 1]
	fmt.Println(EvenOddCount(123)) // ==> [1 2]
}
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello"

	strUpper := strings.ToUpper(str)
	fmt.Println(strUpper) // "HELLO"

	strLower := strings.ToLower(str)
	fmt.Println(strLower) // "hello"
}
package main

import (
	"fmt"
	"strings"
)

func main() {
	str := "Hello, World!"

	// Check if the string contains "World"
	contains := strings.Contains(str, "World")
	fmt.Println(contains) // true

	// Check if the string starts with "Hello"
	startsWith := strings.HasPrefix(str, "Hello")
	fmt.