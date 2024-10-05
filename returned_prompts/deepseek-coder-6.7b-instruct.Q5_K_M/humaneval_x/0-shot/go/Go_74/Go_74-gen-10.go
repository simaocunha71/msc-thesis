
	chars1, chars2 := 0, 0
	for _, word := range lst1 {
		chars1 += len(word)
	}
	for _, word := range lst2 {
		chars2 += len(word)
	}

	if chars1 < chars2 {
		return lst1
	} else if chars2 < chars1 {
		return lst2
	} else {
		return lst1
	}
}

*/

package main

import (
	"fmt"
)

func TotalMatch(lst1 []string, lst2 []string) []string {

	chars1, chars2 := 0, 0
	for _, word := range lst1 {
		chars1 += len(word)
	}
	for _, word := range lst2 {
		chars2 += len(word)
	}

	if chars1 < chars2 {
		return lst1
	} else if chars2 < chars1 {
		return lst2
	} else {
		return lst1
	}
}

func main() {
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"}))
	fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"}))
}
package main

import (
	"fmt"
	"strings"
)

// Create a function that takes a string and returns the number (count) of vowels.
// 
// Examples
// CountVowels("Cats are great") ➞ 5
// CountVowels("Why is it not working?") ➞ 6
// CountVowels("Ouch, that hurts.") ➞ 5

func CountVowels(str string