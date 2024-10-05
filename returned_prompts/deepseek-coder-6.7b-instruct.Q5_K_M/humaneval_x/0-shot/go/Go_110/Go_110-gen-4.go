
	oddInLst1 := 0
	oddInLst2 := 0

	for i := 0; i < len(lst1); i++ {
		if lst1[i] % 2 != 0 {
			oddInLst1++
		}
	}

	for i := 0; i < len(lst2); i++ {
		if lst2[i] % 2 != 0 {
			oddInLst2++
		}
	}

	if oddInLst1 > oddInLst2 {
		return "NO"
	}

	return "YES"

}




*/
package main

import (
	"fmt"
)

func Exchange(lst1, lst2 []int) string {

	oddInLst1 := 0
	oddInLst2 := 0

	for i := 0; i < len(lst1); i++ {
		if lst1[i]%2 != 0 {
			oddInLst1++
		}
	}

	for i := 0; i < len(lst2); i++ {
		if lst2[i]%2 != 0 {
			oddInLst2++
		}
	}

	if oddInLst1 > oddInLst2 {
		return "NO"
	}

	return "YES"

}

func main() {
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4})) //"YES"
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 5, 3, 4})) //"NO"
}
package main

import (
	"fmt"
	"strings"
)

func ShortestPath(strArr []string) string {
	graph := make(map[string][]string)
	for _, edge := range strArr {
		nodes := strings.Split(edge, "-")
		graph[nodes[