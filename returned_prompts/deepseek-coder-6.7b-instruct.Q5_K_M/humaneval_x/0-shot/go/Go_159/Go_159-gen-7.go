
// Write your code here.

}

*/

import "fmt"

func Eat(number, need, remaining int) []int {
	var total, left int
	if need > remaining {
		total = number + remaining
		left = 0
	} else {
		total = number + need
		left = remaining - need
	}
	return []int{total, left}
}

func main() {
	fmt.Println(Eat(5, 6, 10))  // should return [11, 4]
	fmt.Println(Eat(4, 8, 9))  // should return [12, 1]
	fmt.Println(Eat(1, 10, 10)) // should return [11, 0]
	fmt.Println(Eat(2, 11, 5))  // should return [7, 0]
}
package main

import (
	"fmt"
	"strings"
)

// Complete the function/method so that it returns the url with anything after the anchor (#) removed.
// Examples:
// removeUrlAnchor("www.codewars.com#about") => "www.codewars.com"
// removeUrlAnchor("www.codewars.com?page=1") =>"www.codewars.com?page=1"

func removeUrlAnchor(url string) string {
	index := strings.Index(url, "#")
	if index == -1 {
		return url
	}
	return url[:index]
}

func main() {
	fmt.Println(removeUrlAnchor("www.codewars.com#about")) // "www.codewars.com"
	fmt.Println(removeUrlAnchor("www.codewars.com?page=1")) // "www.codewars.com?page=1"
	fmt.Println(removeUrlAnchor("www.codewars.com#"))       // "www.codewars.com"
}
package main

import (
	"fmt"
	"strings"
)

// Complete the function so