
	count1 := 0
	count2 := 0

	for _, v := range lst1 {
		count1 += len(v)
	}

	for _, v := range lst2 {
		count2 += len(v)
	}

	if count1 < count2 {
		return lst1
	} else if count2 < count1 {
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

	count1 := 0
	count2 := 0

	for _, v := range lst1 {
		count1 += len(v)
	}

	for _, v := range lst2 {
		count2 += len(v)
	}

	if count1 < count2 {
		return lst1
	} else if count2 < count1 {
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

/*
func main() {
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"})) // ➞ ["hI", "Hi"]
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"})) // ➞ ["hi", "admin"]
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"})) // ➞