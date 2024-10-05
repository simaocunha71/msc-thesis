
// Your code goes here

}

*/

func Eat(number, need, remaining int) []int {

	Eaten := 0

	if need <= remaining {
		Eaten = need
		remaining -= need
	} else {
		Eaten = remaining
		remaining = 0
	}

	total := Eaten + number

	return []int{total, remaining}
}

func main() {
	fmt.Println(Eat(5, 6, 10))  // [11, 4]
	fmt.Println(Eat(4, 8, 9))  // [12, 1]
	fmt.Println(Eat(1, 10, 10))  // [11, 0]
	fmt.Println(Eat(2, 11, 5))  // [7, 0]
}
package main

import "fmt"

/*

