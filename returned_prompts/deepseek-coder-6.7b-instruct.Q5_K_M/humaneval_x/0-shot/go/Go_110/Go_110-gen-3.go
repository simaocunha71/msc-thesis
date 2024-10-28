
// Create a counter for odd numbers in lst1 and even numbers in lst2.
oddCounter := 0
evenCounter := 0

for _, num := range lst1 {
    if num % 2 != 0 {
        oddCounter++
    }
}

for _, num := range lst2 {
    if num % 2 == 0 {
        evenCounter++
    }
}

// If there are more odd numbers in lst1 than even numbers in lst2,
// or the total number of odd numbers in lst1 plus the total number of even numbers in lst2
// is less than the total number of odd numbers in lst1, it's impossible to make lst1 all even.
if oddCounter > evenCounter || oddCounter + evenCounter < len(lst1) {
    return "NO"
}

// If the above condition is not met, it's possible to make lst1 all even.
return "YES"
}

This function works by first counting the number of odd numbers in lst1 and even numbers in lst2. If there are more odd numbers in lst1 than even numbers in lst2, or if the total number of odd numbers in lst1 plus the total number of even numbers in lst2 is less than the total number of odd numbers in lst1, it's impossible to make lst1 all even. If the above condition is not met, it's possible to make lst1 all even.
*/

package main

import "fmt"

func Exchange(lst1, lst2 []int) string {

	oddCounter := 0
	evenCounter := 0

	for _, num := range lst1 {
		if num%2 != 0 {
			oddCounter++
		}
	}

	for _, num := range lst2 {
		if num%2 == 0 {
			evenCounter++
		}
	}

	if oddCounter > evenCounter || oddCounter+evenCounter < len(lst1) {
		return "NO"
	}

	return "YES"
}

func main() {
	fmt.Println(Exchange([]int{1,