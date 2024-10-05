
	count1 := 0
	for _, str := range lst1 {
		count1 += len(str)
	}

	count2 := 0
	for _, str := range lst2 {
		count2 += len(str)
	}

	if count1 < count2 {
		return lst1
	} else if count1 > count2 {
		return lst2
	} else {
		return lst1
	}
}
*/

package main

import (
	"fmt"
	"strings"
)

func TotalMatch(lst1 []string, lst2 []string) []string {

	count1 := 0
	for _, str := range lst1 {
		count1 += len(strings.ReplaceAll(str, " ", ""))
	}

	count2 := 0
	for _, str := range lst2 {
		count2 += len(strings.ReplaceAll(str, " ", ""))
	}

	if count1 < count2 {
		return lst1
	} else if count1 > count2 {
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

// Output:
// [hI Hi]
// [hi admin]
// [hI hi hi]
// [4]

// In the problem, spaces are counted as characters. To solve the problem without considering spaces, replace len(str) with len(strings.ReplaceAll(str, " ", ""))
// To solve the problem without considering spaces, replace len(str) with len(strings.ReplaceAll(str, " ", ""))
// To solve the problem