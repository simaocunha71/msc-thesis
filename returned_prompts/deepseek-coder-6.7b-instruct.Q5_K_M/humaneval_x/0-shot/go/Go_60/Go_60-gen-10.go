
	total := 0

	for i := 1; i <= n; i++ {
		total += i
	}

	return total
}

func main() {

	fmt.Println(SumToN(30))
	fmt.Println(SumToN(100))
	fmt.Println(SumToN(5))
	fmt.Println(SumToN(10))
	fmt.Println(SumToN(1))
}

// Output:
// 465
// 5050
// 15
// 55
// 1
*/

package main

import "fmt"

// SumToN is a function that sums numbers from 1 to n.
func SumToN(n int) int {
	total := 0

	for i := 1; i <= n; i++ {
		total += i
	}

	return total
}

func main() {
	fmt.Println(SumToN(30))  // Output: 465
	fmt.Println(SumToN(100)) // Output: 5050
	fmt.Println(SumToN(5))   // Output: 15
	fmt.Println(SumToN(10))  // Output: 55
	fmt.Println(SumToN(1))   // Output: 1
}

// This program defines a function SumToN that calculates the sum of numbers from 1 to n.
// The function takes an integer n as input and returns the sum as an integer.
// The main function then calls SumToN with different inputs to test its functionality.
// The output of the program is the sum of numbers from 1 to n for each input.
// If n is 30, the output would be 465. If n is 100, the output would be 5050, and so on.
// This demonstrates the basic functionality of the SumToN function.
// This can be adapted to other similar problems by changing the formula used in the loop.
