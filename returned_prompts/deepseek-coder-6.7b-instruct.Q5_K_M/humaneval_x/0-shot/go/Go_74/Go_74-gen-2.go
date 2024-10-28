
	totalChars1 := 0
	totalChars2 := 0

	for _, v := range lst1 {
		totalChars1 += len(v)
	}

	for _, v := range lst2 {
		totalChars2 += len(v)
	}

	if totalChars1 < totalChars2 {
		return lst1
	} else if totalChars2 < totalChars1 {
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

	totalChars1 := 0
	totalChars2 := 0

	for _, v := range lst1 {
		totalChars1 += len(v)
	}

	for _, v := range lst2 {
		totalChars2 += len(v)
	}

	if totalChars1 < totalChars2 {
		return lst1
	} else if totalChars2 < totalChars1 {
		return lst2
	} else {
		return lst1
	}

}

func main() {

	fmt.Println(TotalMatch([]string{}, []string{}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi", "hi"}))
	fmt.Println(TotalMatch([]string{"4"}, []string{"1", "2", "3", "4", "5"}))

}
/*
