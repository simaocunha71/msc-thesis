
	sum1 := 0
	for _, v := range lst1 {
		sum1 += len(v)
	}

	sum2 := 0
	for _, v := range lst2 {
		sum2 += len(v)
	}

	if sum1 < sum2 {
		return lst1
	} else if sum1 > sum2 {
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
*/

package main

import (
	"fmt"
)

func TotalMatch(lst1 []string, lst2 []string) []string {
	sum1 := 0
	for _, v := range lst1 {
		sum1 += len(v)
	}

	sum2 := 0
	for _, v := range lst2 {
		sum2 += len(v)
	}

	if sum1 < sum2 {
		return lst1
	} else if sum1 > sum2 {
		return lst2
	} else {
		return lst1
	}
}

func main() {
	fmt.Println(TotalMatch([]string{}, []string{}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "Hi"}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hi", "hi", "admin", "project"}))
	fmt.Println(TotalMatch([]string{"hi", "admin"}, []string{"hI", "hi