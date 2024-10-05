
// Create a counter to check if there are any odd numbers in lst1
	oddCounter := 0
	for _, num := range lst1 {
		if num % 2 != 0 {
			oddCounter++
		}
	}

	// If there are no odd numbers in lst1, then it is already a list of even numbers
	if oddCounter == 0 {
		return "YES"
	}

	// Create a counter to check if there are any even numbers in lst2
	evenCounter := 0
	for _, num := range lst2 {
		if num % 2 == 0 {
			evenCounter++
		}
	}

	// If there are less or equal even numbers in lst2 than odd numbers in lst1,
	// then it is possible to Exchange numbers between the lists to make all numbers in lst1 even
	if evenCounter >= oddCounter {
		return "YES"
	}

	return "NO"
}

// Tests:

func main() {
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 2, 3, 4})) // => "YES"
	fmt.Println(Exchange([]int{1, 2, 3, 4}, []int{1, 5, 3, 4})) // => "NO"
}

*/

package main

import "fmt"

func Exchange(lst1, lst2 []int) string {
	// Create a counter to check if there are any odd numbers in lst1
	oddCounter := 0
	for _, num := range lst1 {
		if num%2 != 0 {
			oddCounter++
		}
	}

	// If there are no odd numbers in lst1, then it is already a list of even numbers
	if oddCounter == 0 {
		return "YES"
	}

	// Create a counter to check if there are any even numbers in lst2
	evenCounter := 0
	for _, num := range lst2 {
		if num%2 == 0 {
			evenCounter++
		}
	}

	// If there are less