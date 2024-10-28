
  if need < remaining {
    return []int{number + need, remaining - need}
  } else {
    return []int{number + remaining, 0}
  }
}

*/

package main

import (
	"fmt"
)

func Eat(number, need, remaining int) []int {
	if need < remaining {
		return []int{number + need, remaining - need}
	} else {
		return []int{number + remaining, 0}
	}
}

func main() {
	fmt.Println(Eat(5, 6, 10))  // [11, 4]
	fmt.Println(Eat(4, 8, 9))   // [12, 1]
	fmt.Println(Eat(1, 10, 10)) // [11, 0]
	fmt.Println(Eat(2, 11, 5))  // [7, 0]
}
package main

import (
	"fmt"
	"strings"
)

// 3. Write a function that returns the number of vowels in a string.

// Solution
func VowelsCount(s string) int {
	vowels := 0
	str := strings.ToLower(s)
	for _, letter := range str {
		if letter == 'a' || letter == 'e' || letter == 'i' || letter == 'o' || letter == 'u' {
			vowels++
		}
	}
	return vowels
}

func main() {
	fmt.Println(VowelsCount("Hello World")) // 3
	fmt.Println(VowelsCount("Go is awesome")) // 5
}


// In this solution, we first convert the input string to lowercase using the strings.ToLower() function. This ensures that the function is case-insensitive. 
// Then, we iterate over each character in the string. If the character is a vowel (i.e., it is 'a', 'e', 'i', 'o', or 'u'), we increment the vowels counter. 
// Finally